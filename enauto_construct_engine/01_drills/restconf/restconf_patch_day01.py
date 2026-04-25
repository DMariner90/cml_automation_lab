import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from rich import print

urllib3.disable_warnings()

DEVICEIP = "10.229.1.13"
USERNAME = "admin"
PASSWORD = "admin"

PATCH_INT_DESCRIPTION_URL = f"https://{DEVICEIP}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1"
VERIFY_URL = f"https://{DEVICEIP}/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"

HEADERS = {
   "Accept": "application/yang-data+json",
   "Content-Type": "application/yang-data+json"
}

PAYLOAD = {
   "Cisco-IOS-XE-native:GigabitEthernet": {
      "name":"1",
      "description":"INTERFACE_TO_EXTERNAL"
   }
}

PATCH_response = requests.patch(
   url=PATCH_INT_DESCRIPTION_URL, 
   headers=HEADERS, 
   auth=HTTPBasicAuth(USERNAME,PASSWORD),
   data=json.dumps(PAYLOAD),
   verify=False
)

print("PATCH STATUS:", PATCH_response.status_code)



VERIFY_response = requests.get(
   url=VERIFY_URL, 
   headers=HEADERS, 
   auth=HTTPBasicAuth(USERNAME,PASSWORD), 
   verify=False
)

print("VERIFY STATUS:", VERIFY_response.status_code)
print(json.dumps(VERIFY_response.json(), indent=4))

   