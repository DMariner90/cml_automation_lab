import requests
import urllib3
from rich import print
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://10.10.20.85"
AUTHENTICATION_URL = BASE_URL + "/dna/system/api/v1/auth/token"
DEVICES_URL = BASE_URL + "/dna/intent/api/v1/network-device"
COMMAND_RUNNER = BASE_URL + "/dna/intent/api/v1/network-device-poller/cli/read-request"
USERNAME = "administrator"
PASSWORD = "Cisco1234!"

authentication_request = requests.post(url=AUTHENTICATION_URL, auth=(USERNAME, PASSWORD), verify=False).json()
auth_token = authentication_request["Token"]


HEADERS = {
	"x-auth-token": auth_token,
	"Accept": "application/json",
	"Content-Type": "application/json"
}


device_id_request = requests.get(url=DEVICES_URL, auth=(USERNAME, PASSWORD), verify=False).json()
print(device_id_request)