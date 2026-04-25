import requests
from getpass import getpass
import urllib3
import yaml

# Disable SSL warnings for lab boxes with self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Define your devices here ---
# Adjust IPs/names to match your lab
DEVICES = [
    {"name": "R1", "ip": "10.229.1.11"},
    {"name": "R2", "ip": "10.229.1.12"},
    {"name": "R3", "ip": "10.229.1.13"},
]

RESTCONF_RESOURCE = "/restconf/data/ietf-interfaces:interfaces"
HEADERS = {"Accept": "application/yang-data+json"}


def main():
    print("=== RESTCONF: Get interfaces from all routers ===")
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    for device in DEVICES:
        name = device["name"]
        ip = device["ip"]
        url = f"https://{ip}{RESTCONF_RESOURCE}"

        print(f"\n--- {name} ({ip}) ---")
        try:
            resp = requests.get(
                url,
                headers=HEADERS,
                auth=(username, password),
                verify=False,
                timeout=10,
            )
        except requests.RequestException as exc:
            print(f"Request error for {name}: {exc}")
            continue

        print(f"HTTP Status: {resp.status_code}")
        if not resp.ok:
            print(f"Skipping {name}, non-OK response.")
            continue

        # Parse JSON from RESTCONF response
        try:
            data = resp.json()
        except ValueError as exc:
            print(f"Failed to parse JSON from {name}: {exc}")
            continue

        # Convert JSON -> YAML string
        yaml_output = yaml.safe_dump(data, sort_keys=False)

        # Print a little preview
        print("YAML preview (first 20 lines):")
        for i, line in enumerate(yaml_output.splitlines()):
            if i >= 20:
                print("... (truncated)")
                break
            print(line)

        # Save to file per device
        filename = f"{name.lower()}_interfaces.yaml"
        with open(filename, "w") as f:
            f.write(yaml_output)

        print(f"Saved YAML to {filename}")


if __name__ == "__main__":
    main()
