import requests
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print

urllib3.disable_warnings()

url = "https://10.229.1.13/restconf/data/ietf-interfaces:interfaces"

headers = {
    "Accept": "application/yang-data+json",
    "Content_Type": "application/json"
}


response = requests.get(url=url, headers=headers, auth=HTTPBasicAuth("admin","admin"), verify=False)

raw_json_data = response.json()
print(raw_json_data)


for interface in raw_json_data["ietf-interfaces:interfaces"]["interface"]:
    name = interface["name"]
    enabled = interface["enabled"]
    print(f"NAME: {name} : ENABLED {enabled}")