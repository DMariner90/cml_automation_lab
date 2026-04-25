import requests
from rich import print


meraki_key = "a8a49bd8da5dbb6f8f5dcca0a2c9d0aeba340049"
org_url = "https://api.meraki.com/api/v1/organizations"


headers = {
        "Authorization": f"Bearer {meraki_key}"
}


org_response = requests.get(url=org_url, headers=headers).json()
for org in org_response:
    if org['name'] == "DevNet-sExy0LYznaM1":
        org_id = org["id"]
print(org_id)

networks_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/networks"

payload = {

        "name": "Daves Test Network",
        "productTypes": ["appliance", "switch", "wireless"],
        "timeZone": "America/Los_Angeles",
        "notes": "This is my test network"
}


new_network_response = requests.post(url=networks_url, headers=headers, json=payload)
print(new_network_response)
