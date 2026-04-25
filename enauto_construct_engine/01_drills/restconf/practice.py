import requests
import urllib3
from requests.auth import HTTPBasicAuth
from rich import print

urllib3.disable_warnings()

RESTCONF_RTR_IP = "10.229.1.13"
USERNAME = "admin"
PASSWORD = "admin"

INTERFACES_URL = f"https://{RESTCONF_RTR_IP}/restconf/data/ietf-interfaces:interfaces"

HEADERS = {
        "Accept": "application/yang-data+json"
}

api_response = requests.get(url=INTERFACES_URL, headers=HEADERS, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify=False)

print(f"Status Code: {api_response.status_code}")

interfaces_data  = api_response.json()
print(interfaces_data)

for interface in interfaces_data["ietf-interfaces:interfaces"]["interface"]:
        NAME = interface["name"]
        TYPE = interface["type"]
        ENABLED = interface["enabled"]
        
        print(f"NAME: {NAME}")
        print(f"TYPE: {TYPE}")
        print(f"ENABLED: {ENABLED}")

        