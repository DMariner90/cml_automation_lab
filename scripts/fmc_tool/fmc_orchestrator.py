#!/usr/bin/env python3
"""
FMC ORCHESTRATOR
================

Shared engine used by all FMC tasks.

Responsibilities:
- Authentication
- Domain discovery & selection
- Policy discovery & selection
- Device discovery & selection
- Pagination handling (offset/limit)
- Per-run output folder creation
- YAML/JSON output writing
- Run log tracking for multi-task runs

NOTE:
- Username/password are NEVER stored on disk
- Output format is chosen at runtime (YAML default)
"""

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
import urllib3

# Disable SSL warnings (lab FMCs commonly use self-signed certs)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------------------------------------------------------------------
# FMC SETTINGS
# ---------------------------------------------------------------------------
FMC_HOST = "10.10.20.62"  # <-- change if needed
BASE_URL = f"https://{FMC_HOST}"

DEFAULT_LIMIT = 100
OUTPUTS_ROOT = Path(__file__).parent / "outputs"


# ---------------------------------------------------------------------------
# Run Context Object
# ---------------------------------------------------------------------------
@dataclass
class RunContext:
    """
    Holds run-specific state shared across tasks.
    """

    output_format: str  # "yaml" or "json"
    run_dir: Path  # outputs/<timestamp__domain...>/
    domain_name: str
    domain_uuid: str
    fmc_host: str


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------
def _timestamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def _slugify(text: str, max_len: int = 80) -> str:
    """
    Make strings safe for filenames.
    """
    text = text.strip().replace(" ", "_")
    text = re.sub(r"[^A-Za-z0-9_.\-]+", "", text)
    return text[:max_len]


# ---------------------------------------------------------------------------
# Output handling
# ---------------------------------------------------------------------------
def create_run_folder(domain_name: str, domain_uuid: str) -> Path:
    """
    Create per-run folder:

      outputs/<timestamp>__domain-<name>__uuid-<uuid>/
    """
    OUTPUTS_ROOT.mkdir(parents=True, exist_ok=True)

    folder = (
        f"{_timestamp()}__domain-{_slugify(domain_name)}"
        f"__uuid-{_slugify(domain_uuid, 36)}"
    )

    run_dir = OUTPUTS_ROOT / folder
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def write_output(ctx: RunContext, file_stem: str, payload: Any) -> Path:
    """
    Write task output into the run folder.

    - YAML is default (easier to read)
    - JSON optional (exact API fidelity)

    file_stem examples:
      get_rules__policy-Internet_Edge
      get_interfaces__device-FTD01
    """
    stem = _slugify(file_stem)

    if ctx.output_format == "json":
        out_path = ctx.run_dir / f"{stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        return out_path

    # YAML default
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        raise SystemExit(
            "YAML output selected but PyYAML is not installed.\n"
            "Install it with:\n"
            "  pip install pyyaml"
        )

    out_path = ctx.run_dir / f"{stem}.yaml"
    with open(out_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(payload, f, sort_keys=False)
    return out_path


def append_run_log(ctx: RunContext, entry: Dict[str, Any]) -> Path:
    """
    Append an entry to run_log.yaml (or .json fallback).

    Used to track:
    - which tasks ran
    - selections made
    - output formats
    """
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "fmc_host": ctx.fmc_host,
        "domain": {
            "name": ctx.domain_name,
            "uuid": ctx.domain_uuid,
        },
        **entry,
    }

    log_yaml = ctx.run_dir / "run_log.yaml"
    log_json = ctx.run_dir / "run_log.json"

    try:
        import yaml  # type: ignore

        if log_yaml.exists():
            with open(log_yaml, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or []
        else:
            data = []

        if not isinstance(data, list):
            data = [data]

        data.append(log_entry)

        with open(log_yaml, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False)

        return log_yaml

    except ModuleNotFoundError:
        # JSON fallback
        if log_json.exists():
            with open(log_json, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []

        if not isinstance(data, list):
            data = [data]

        data.append(log_entry)

        with open(log_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        return log_json


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------
def fmc_authenticate(username: str, password: str) -> str:
    """
    Authenticate to FMC and return access token.
    """
    url = f"{BASE_URL}/api/fmc_platform/v1/auth/generatetoken"
    print(f"Authenticating to FMC at {url}")

    resp = requests.post(
        url,
        auth=(username, password),
        verify=False,
    )

    if resp.status_code != 204:
        print(f"Authentication failed: HTTP {resp.status_code}")
        print(resp.text)
        raise SystemExit(1)

    return resp.headers["X-auth-access-token"]


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------
def fmc_get_all_items(
    access_token: str,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    limit: int = DEFAULT_LIMIT,
) -> Any:
    """
    Retrieve all items from an FMC collection endpoint using offset/limit.

    If the response does NOT contain "items", the full JSON body is returned.
    """
    headers = {
        "Accept": "application/json",
        "X-auth-access-token": access_token,
    }

    params = params or {}
    offset = 0
    all_items: List[Any] = []

    while True:
        page_params = dict(params)
        page_params["offset"] = offset
        page_params["limit"] = limit

        print(f"GET {url} (offset={offset}, limit={limit})")
        resp = requests.get(url, headers=headers, params=page_params, verify=False)

        if not resp.ok:
            print(f"Request failed: HTTP {resp.status_code}")
            print(resp.text)
            raise SystemExit(1)

        data = resp.json()

        if "items" not in data:
            return data

        items = data.get("items", [])
        all_items.extend(items)

        if len(items) < limit:
            break

        offset += limit

    return all_items


# ---------------------------------------------------------------------------
# Domain handling
# ---------------------------------------------------------------------------
def fmc_list_domains(access_token: str) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/api/fmc_platform/v1/domain"
    headers = {"Accept": "application/json", "X-auth-access-token": access_token}

    resp = requests.get(url, headers=headers, verify=False)
    if not resp.ok:
        print(f"Failed to retrieve domains: HTTP {resp.status_code}")
        raise SystemExit(1)

    return [
        {"name": d["name"], "uuid": d["uuid"], "type": d["type"]}
        for d in resp.json().get("items", [])
    ]


def select_domain(domains: List[Dict[str, Any]]) -> Dict[str, Any]:
    print("\n=== Available FMC Domains ===")
    for i, d in enumerate(domains, start=1):
        print(f"{i}) {d['name']}  |  UUID: {d['uuid']}")

    while True:
        choice = input("Select domain by number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(domains):
            return domains[int(choice) - 1]
        print("Invalid selection.")


# ---------------------------------------------------------------------------
# Policies
# ---------------------------------------------------------------------------
def fmc_list_policies(access_token: str, domain_uuid: str) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies"
    data = fmc_get_all_items(access_token, url)
    return [{"name": p["name"], "id": p["id"], "type": p["type"]} for p in data]


def select_policies(policies: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], str]:
    print("\n=== Access Policies ===")
    for i, p in enumerate(policies, start=1):
        print(f"{i}. {p['name']}")

    choice = input("\nSelect policies (Enter/all or 1,3,5): ").strip()

    if choice == "" or choice.lower() == "all":
        return policies, "all"

    indexes = [int(x) for x in choice.split(",") if x.strip().isdigit()]
    selected = [policies[i - 1] for i in indexes if 1 <= i <= len(policies)]
    return selected, f"indexes={indexes}"


# ---------------------------------------------------------------------------
# Devices
# ---------------------------------------------------------------------------
def fmc_list_devices(access_token: str, domain_uuid: str) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/api/fmc_config/v1/domain/{domain_uuid}/device/devicerecords"
    data = fmc_get_all_items(access_token, url)

    return [
        {
            "name": d["name"],
            "id": d["id"],
            "model": d.get("model"),
            "hostName": d.get("hostName"),
        }
        for d in data
    ]


def select_devices(devices: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], str]:
    print("\n=== Devices ===")
    for i, d in enumerate(devices, start=1):
        print(f"{i}. {d['name']} ({d.get('model')})")

    choice = input("\nSelect devices (Enter/all or 1,3,5): ").strip()

    if choice == "" or choice.lower() == "all":
        return devices, "all"

    indexes = [int(x) for x in choice.split(",") if x.strip().isdigit()]
    selected = [devices[i - 1] for i in indexes if 1 <= i <= len(devices)]
    return selected, f"indexes={indexes}"
