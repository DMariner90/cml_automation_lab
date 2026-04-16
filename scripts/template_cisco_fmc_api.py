#!/usr/bin/env python3

"""
CISCO FMC GENERIC API TEMPLATE (DOMAIN SELECT ONLY)
---------------------------------------------------
This script:

1) Authenticates to Cisco FMC using:
      POST /api/fmc_platform/v1/auth/generatetoken

2) Retrieves the list of domains from:
      GET /api/fmc_platform/v1/domain

3) Prints the domains (name + UUID) and saves them to a file:
      fmc_domains.txt

4) Prompts you to select a domain by number.

5) Performs a single API call (GET/POST/PUT/DELETE) against an endpoint
   that includes the chosen domain UUID.

You customise:
- FMC_HOST
- ENDPOINT_PATH_TEMPLATE
- HTTP_METHOD
- JSON_BODY (for POST/PUT)
"""

import requests
import urllib3
import json
from getpass import getpass

# Ignore SSL warnings for lab FMC (self-signed certs, etc.)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------------------------------------------------------------------
# FMC SETTINGS — CHANGE THESE
# ---------------------------------------------------------------------------
FMC_HOST = "10.10.20.62"          # <-- your FMC IP / hostname
BASE_URL = f"https://{FMC_HOST}"

# Endpoint template: {domain_uuid} will be replaced after selection
# Examples:
#   "/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies"
#   "/api/fmc_config/v1/domain/{domain_uuid}/object/networks"
ENDPOINT_PATH_TEMPLATE = "/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies"

# HTTP method to use: "GET", "POST", "PUT", "DELETE"
HTTP_METHOD = "GET"

# JSON body for POST / PUT (set to None for GET / DELETE)
JSON_BODY = None
# Example:
# JSON_BODY = {
#     "type": "AccessPolicy",
#     "name": "Lab-Policy",
#     "description": "Created via generic FMC template"
# }


# ---------------------------------------------------------------------------
# AUTHENTICATION
# ---------------------------------------------------------------------------
def fmc_authenticate(username: str, password: str):
    """
    Authenticate to FMC and return the access token.

    FMC auth endpoint:
      POST /api/fmc_platform/v1/auth/generatetoken

    Successful auth returns:
      - HTTP 204
      - access token in header "X-auth-access-token"
    """
    auth_url = f"{BASE_URL}/api/fmc_platform/v1/auth/generatetoken"
    print(f"Authenticating to FMC at: {auth_url}")

    resp = requests.post(
        auth_url,
        auth=(username, password),   # HTTP Basic auth
        verify=False,
    )

    if resp.status_code != 204:
        print(f"Authentication failed: HTTP {resp.status_code}")
        print(resp.text)
        raise SystemExit(1)

    access_token = resp.headers.get("X-auth-access-token")
    refresh_token = resp.headers.get("X-auth-refresh-token")
    header_domain_uuid = resp.headers.get("DOMAIN_UUID")

    print(f"Access Token : {access_token}")
    print(f"Refresh Token: {refresh_token}")
    print(f"Header Domain UUID (may or may not be set): {header_domain_uuid}")

    return access_token


# ---------------------------------------------------------------------------
# DOMAIN DISCOVERY & SELECTION
# ---------------------------------------------------------------------------
def fmc_list_domains(access_token: str):
    """
    Query FMC for all available domains.

    Endpoint:
      GET /api/fmc_platform/v1/domain

    Returns a list of dicts:
      [{"name": ..., "uuid": ..., "type": ...}, ...]
    """
    url = f"{BASE_URL}/api/fmc_platform/v1/domain"
    headers = {
        "Accept": "application/json",
        "X-auth-access-token": access_token,
    }

    print(f"\nRequesting domain list from: {url}")
    resp = requests.get(url, headers=headers, verify=False)

    if not resp.ok:
        print(f"Failed to retrieve domains: HTTP {resp.status_code}")
        print(resp.text)
        raise SystemExit(1)

    data = resp.json()
    items = data.get("items", [])

    domains = []
    for item in items:
        domains.append(
            {
                "name": item.get("name"),
                "uuid": item.get("uuid"),
                "type": item.get("type"),
            }
        )

    return domains


def select_domain(domains):
    """
    Print domains, save them to a file, and let the user choose one.

    Returns:
      selected domain UUID (string)
    """
    if not domains:
        print("No domains returned from FMC. Exiting.")
        raise SystemExit(1)

    print("\n=== Available FMC Domains ===")

    # Build a human-readable output string to print and save
    lines = []
    for index, domain in enumerate(domains, start=1):
        line = f"{index}) {domain['name']}  |  UUID: {domain['uuid']}  |  Type: {domain['type']}"
        lines.append(line)
        print(line)

    # Save the domain list to a file for later reference
    filename = "fmc_domains.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("FMC Domains (Name / UUID / Type)\n")
        f.write("-" * 60 + "\n")
        for line in lines:
            f.write(line + "\n")

    print(f"\nDomain list saved to {filename}")

    # Prompt user to choose a domain by number
    while True:
        choice = input("Select domain by number: ")
        try:
            index = int(choice)
            if 1 <= index <= len(domains):
                selected = domains[index - 1]
                print(f"Selected domain: {selected['name']} ({selected['uuid']})")
                return selected["uuid"]
            else:
                print("Invalid selection: number out of range.")
        except ValueError:
            print("Please enter a valid number.")


# ---------------------------------------------------------------------------
# GENERIC FMC API CALL
# ---------------------------------------------------------------------------
def fmc_api_call(method: str, url: str, access_token: str, body=None):
    """
    Generic FMC API call function.

    Args:
      method       : "GET", "POST", "PUT", "DELETE"
      url          : full URL including domain UUID
      access_token : FMC access token string
      body         : Python dict for JSON payload (POST/PUT), or None
    """
    headers = {
        "Accept": "application/json",
        "X-auth-access-token": access_token,
    }

    # Only add Content-Type if we are actually sending JSON
    if method.upper() in ("POST", "PUT") and body is not None:
        headers["Content-Type"] = "application/json"

    print("\n--- FMC API CALL ---")
    print(f"Method : {method}")
    print(f"URL    : {url}")
    print(f"Headers: {headers}")
    if body is not None:
        print("JSON Body:")
        print(json.dumps(body, indent=2))

    resp = requests.request(
        method=method.upper(),
        url=url,
        headers=headers,
        json=body,
        verify=False,
    )

    print(f"\nHTTP Status: {resp.status_code}")

    # Try pretty-print JSON, or show raw text if not JSON
    try:
        data = resp.json()
        print(json.dumps(data, indent=2))
    except ValueError:
        print(resp.text)

    return resp


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    print("=== Cisco FMC Generic API Template (Domain Select Only) ===")

    username = input("Enter FMC username: ")
    password = getpass("Enter FMC password: ")

    # Step 1: authenticate and get access token
    access_token = fmc_authenticate(username, password)

    # Step 2: get domain list and let user choose one
    domains = fmc_list_domains(access_token)
    domain_uuid = select_domain(domains)

    # Step 3: build endpoint URL with chosen domain UUID
    endpoint_path = ENDPOINT_PATH_TEMPLATE.format(domain_uuid=domain_uuid)
    full_url = f"{BASE_URL}{endpoint_path}"

    # Step 4: perform API call
    fmc_api_call(
        method=HTTP_METHOD,
        url=full_url,
        access_token=access_token,
        body=JSON_BODY,
    )


if __name__ == "__main__":
    main()
