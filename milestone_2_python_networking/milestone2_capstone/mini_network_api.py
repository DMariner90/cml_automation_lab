import os
import json
import yaml
import requests
from requests.exceptions import RequestException

# --- Connection parameters ---
device = {
    "host": "sandbox-iosxe-recomm-1.cisco.com",  # NOTE: retired; will likely 401
    "port": 443,
    "username": "developer",
    "password": "C1sco12345",
}

# Build RESTCONF URL (fix: https:// not https//)
url = f"https://{device['host']}:{device['port']}/restconf/data/ietf-interfaces:interfaces"

# Ask for YANG-modeled JSON
headers = {"Accept": "application/yang-data+json"}

# Make the request safely
data = {}  # ensure it's defined even on errors
try:
    resp = requests.get(
        url,
        headers=headers,
        auth=(device["username"], device["password"]),
        verify=False,        # lab only; verify certs in prod
        timeout=15
    )
    print(f"HTTP {resp.status_code} {resp.reason}")
    resp.raise_for_status()
    data = resp.json()
    print("✅ API request successful")
except RequestException as err:
    print(f"❌ API request failed: {err}")
    # Optional: supply mock data so you can practice parsing even if API is down
    data = {
        "ietf-interfaces:interfaces": {
            "interface": [
                {
                    "name": "GigabitEthernet1",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": True,
                    "ietf-ip:ipv4": {"address": [{"ip": "10.10.20.48"}]},
                },
                {
                    "name": "Loopback0",
                    "type": "iana-if-type:softwareLoopback",
                    "enabled": True,
                    "ietf-ip:ipv4": {"address": [{"ip": "172.16.1.1"}]},
                },
                {
                    "name": "GigabitEthernet2",
                    "type": "iana-if-type:ethernetCsmacd",
                    "enabled": False,
                },
            ]
        }
    }
    print("ℹ️ Using mock data for parsing practice")

# Parse interface list safely
interfaces = data.get("ietf-interfaces:interfaces", {}).get("interface", [])
print(f"🧩 Found {len(interfaces)} interfaces")

enabled_ipv4 = []

for interface in interfaces:
    # Pull fields with safe defaults
    name = interface.get("name", "UNKNOWN")
    if_type = interface.get("type", "unknown")
    enabled = bool(interface.get("enabled", False))
    ip = interface.get("ietf-ip:ipv4", {}).get("address", [{}])[0].get("ip", "N/A")

    # Human-readable summary
    print(f"- {name} ({if_type}) enabled={enabled} ipv4={ip}")

    # Keep only enabled interfaces with an IPv4 address
    if enabled and ip != "N/A":
        enabled_ipv4.append({"name": name, "type": if_type, "ip": ip})

# Write outputs (put artifacts in labs/)
os.makedirs("labs", exist_ok=True)

# Full raw data to YAML
with open("scripts/milestone2_capstone/interfaces_output.yaml", "w") as f:
    yaml.dump(data, f, sort_keys=False)

# Filtered summary to YAML
with open("scripts/milestone2_capstone/enabled_interfaces.yaml", "w") as f:
    yaml.dump({"count": len(enabled_ipv4), "interfaces": enabled_ipv4}, f, sort_keys=False)

print("📝 Saved: labs/interfaces_output.yaml")
print("📝 Saved: labs/enabled_interfaces.yaml")
