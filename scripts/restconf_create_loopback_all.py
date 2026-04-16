import requests
from getpass import getpass
import urllib3
import json

# Disable SSL warnings for self-signed certs in the lab
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Define your devices and Loopback IPs here ---
DEVICES = [
    {"name": "R1", "ip": "10.229.1.11", "loopback_ip": "10.100.101.1"},
    {"name": "R2", "ip": "10.229.1.12", "loopback_ip": "10.100.101.2"},
    {"name": "R3", "ip": "10.229.1.13", "loopback_ip": "10.100.101.3"},
]

HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

def build_loopback_payload(ip_address: str) -> dict:
    """
    Build the JSON payload for Loopback100 using ietf-interfaces + ietf-ip.
    """
    return {
        "ietf-interfaces:interface": {
            "name": "Loopback100",
            "description": "Configured by RESTCONF (ENAUTO lab)",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip_address,
                        "netmask": "255.255.255.255"
                    }
                ]
            }
        }
    }

def main():
    print("=== RESTCONF: Create/Update Loopback100 on all routers ===")
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    for device in DEVICES:
        name = device["name"]
        ip = device["ip"]
        lo_ip = device["loopback_ip"]

        # Target URL for a *specific* interface (Loopback100)
        # Using PUT so it's idempotent (create or replace)
        url = (
            f"https://{ip}/restconf/data/"
            f"ietf-interfaces:interfaces/interface=Loopback100"
        )

        payload = build_loopback_payload(lo_ip)

        print(f"\n--- {name} ({ip}) ---")
        print(f"Configuring Loopback100 with IP {lo_ip}")





        try:
            resp = requests.put(
                url,
                headers=HEADERS,
                auth=(username, password),
                data=json.dumps(payload),
                verify=False,
                timeout=10,
            )
        except requests.RequestException as exc:
            print(f"Request error for {name}: {exc}")
            continue

        print(f"HTTP Status: {resp.status_code}")

        if resp.status_code in (200, 201, 204):
            print(f"✅ Loopback100 successfully created/updated on {name}")
        else:
            print(f"⚠️ Unexpected response from {name}:")
            print(resp.text)

    print("\nDone. You can verify with SSH:")
    print("  show ip interface brief | include Loopback100")
    print("or via RESTCONF GET on each device.")


if __name__ == "__main__":
    main()
