import requests
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print

urllib3.disable_warnings()

DEVICEIP = "10.229.1.13"
USERNAME = "admin"
PASSWORD = "admin"

INTERFACES_URL = f"https://{DEVICEIP}/restconf/data/Cisco-IOS-XE-native:native"

HEADERS = {
   "Accept": "application/yang-data+json"
}

restconf_response = requests.get(url=INTERFACES_URL, headers=HEADERS, auth=HTTPBasicAuth(USERNAME,PASSWORD), verify=False)

print(restconf_response.status_code)

interfaces_json = restconf_response.json()
print(interfaces_json)


