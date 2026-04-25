import requests
from requests.auth import HTTPBasicAuth
from rich import print


url = "https://10.229.1.13/restconf/data/ietf-interfaces:interfaces"

headers = {"Accept": "application/yang-data+json"}

response = requests.get(url=url, headers=headers, auth=HTTPBasicAuth("admin","admin"), verify=False)

interface_data = response.json()
print(interface_data["ietf-interfaces:interfaces"]["interface"])

for interface in interface_data["ietf-interfaces:interfaces"]["interface"]:
    name = interface["name"]
    print(name)