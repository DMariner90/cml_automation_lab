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

devices_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/devices"

devices_url_response = requests.get(url=devices_url, headers=headers).json()
for device in devices_url_response:
    mac_address = device["mac"]
    serial_number = device["serial"]
    product_type = device["productType"]
    print(f"MAC ADDRESS: {mac_address}")
    print(f"SERAIL NUMBER: {serial_number}")
    print(f"PRODUCT TYPE: {product_type}")
    print("\==============================n")



