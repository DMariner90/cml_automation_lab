#!/usr/bin/env python3

"""
RESTCONF TEMPLATE SCRIPT
------------------------
A simple, reusable template for performing RESTCONF operations (GET, POST, PUT,
PATCH, DELETE) against IOS XE / CML nodes. Includes verbose explanations so the
intent of every line is clear.

To use:
1. Populate the DEVICES list.
2. Set RESTCONF_RESOURCE to the target URI.
3. Choose the HTTP method.
4. (For POST/PUT/PATCH) place your payload into the DATA variable.
"""

import requests
from getpass import getpass
import urllib3
import yaml

# Disable SSL warnings for lab devices using self-signed certs.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------------------------------------------------------------------
# DEVICE INVENTORY
# Add any number of devices here in dictionary format.
# ---------------------------------------------------------------------------
DEVICES = [
    # {"name": "R1", "ip": "10.229.1.11"},
    # {"name": "R2", "ip": "10.229.1.12"},
]

# ---------------------------------------------------------------------------
# RESTCONF RESOURCE
# This is the URI that follows the device's IP.
# Examples:
#   "/restconf/data/ietf-interfaces:interfaces"
#   "/restconf/data/native/interface/GigabitEthernet=1"
# ---------------------------------------------------------------------------
RESTCONF_RESOURCE = ""  # <-- add resource here as a string


# ---------------------------------------------------------------------------
# HTTP METHOD
# Change this to one of: "GET", "POST", "PUT", "PATCH", "DELETE"
# ---------------------------------------------------------------------------
HTTP_METHOD = "GET"


# ---------------------------------------------------------------------------
# (Optional) PAYLOAD for POST/PUT/PATCH requests
# Replace with a Python dict containing your intended config.
# For GET/DELETE, leave as None.
# ---------------------------------------------------------------------------
DATA = None
# Example payload structure:
# DATA = {
#     "ietf-interfaces:interface": {
#         "name": "Loopback99",
#         "type": "iana-if-type:softwareLoopback",
#         "enabled": True,
#         "ietf-ip:ipv4": {
#             "address": [
#                 {"ip": "99.99.99.99", "netmask": "255.255.255.255"}
#             ]
#         }
#     }
# }


# ---------------------------------------------------------------------------
# RESTCONF HEADERS
# Accept header is mandatory. Content-Type is needed for POST/PUT/PATCH.
# ---------------------------------------------------------------------------
HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}


def main():
    """
    MAIN EXECUTION FUNCTION
    Handles:
    - collecting credentials
    - sending RESTCONF requests per device
    - error handling
    - saving YAML output (if response includes JSON)
    """

    print("=== RESTCONF TEMPLATE SCRIPT ===")
    print(f"HTTP Method: {HTTP_METHOD}")
    print(f"Resource: {RESTCONF_RESOURCE}\n")

    username = input("Enter username: ")
    password = getpass("Enter password: ")

    if not DEVICES:
        print("No devices defined. Add entries to the DEVICES list.")
        return

    for device in DEVICES:
        name = device["name"]
        ip = device["ip"]

        # Full RESTCONF URL for the device
        url = f"https://{ip}{RESTCONF_RESOURCE}"

        print(f"\n--- {name} ({ip}) ---")
        print(f"Sending {HTTP_METHOD} to: {url}")

        try:
            # Map Python string "GET" → actual requests.get, etc.
            if HTTP_METHOD == "GET":
                resp = requests.get(url, headers=HEADERS,
                                    auth=(username, password),
                                    verify=False, timeout=10)

            elif HTTP_METHOD == "POST":
                resp = requests.post(url, headers=HEADERS, json=DATA,
                                     auth=(username, password),
                                     verify=False, timeout=10)

            elif HTTP_METHOD == "PUT":
                resp = requests.put(url, headers=HEADERS, json=DATA,
                                    auth=(username, password),
                                    verify=False, timeout=10)

            elif HTTP_METHOD == "PATCH":
                resp = requests.patch(url, headers=HEADERS, json=DATA,
                                      auth=(username, password),
                                      verify=False, timeout=10)

            elif HTTP_METHOD == "DELETE":
                resp = requests.delete(url, headers=HEADERS,
                                       auth=(username, password),
                                       verify=False, timeout=10)

            else:
                print(f"Unsupported method: {HTTP_METHOD}")
                continue

        except requests.RequestException as exc:
            print(f"Connection error for {name}: {exc}")
            continue

        # Show HTTP status
        print(f"Status Code: {resp.status_code}")

        # Non-OK responses
        if not resp.ok:
            print(f"Non-success response:\n{resp.text}")
            continue

        # Try JSON parse / YAML output for readable formatting
        try:
            data = resp.json()
            yaml_output = yaml.safe_dump(data, sort_keys=False)

            preview_lines = yaml_output.splitlines()
            print("\nYAML preview (first 20 lines):")
            for i, line in enumerate(preview_lines):
                if i >= 20:
                    print("... (truncated)")
                    break
                print(line)

            filename = f"{name.lower()}_response.yaml"
            with open(filename, "w") as f:
                f.write(yaml_output)

            print(f"Saved YAML output to {filename}")

        except ValueError:
            # If no JSON (DELETE or empty response), just print raw
            print("No JSON to parse. Raw response:")
            print(resp.text)


if __name__ == "__main__":
    main()

