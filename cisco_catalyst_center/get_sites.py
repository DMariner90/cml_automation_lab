import requests
import urllib3
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTHENTICATION_URL = "https://10.10.20.85/dna/system/api/v1/auth/token"
SITES_URL = "https://10.10.20.85/dna/intent/api/v1/site"
USERNAME = "administrator"
PASSWORD = "Cisco1234!"

authentication_request = requests.post(url=AUTHENTICATION_URL, auth=(USERNAME, PASSWORD), verify=False).json()
auth_token = authentication_request["Token"]


HEADERS = {
	"x-auth-token": auth_token,
	"Accept": "application/json"
}

site_request = requests.get(url=SITES_URL, headers=HEADERS, verify=False).json()
print(site_request)
print(site_request["response"])
print("\n")
print(site_request["response"][0])
print("\n")
print(site_request["response"][0]["instanceTenantId"])
print(site_request["response"][0]["name"])
print(site_request["response"][1]["instanceTenantId"])
print(site_request["response"][1]["name"])
print(site_request["response"][2]["instanceTenantId"])
print(site_request["response"][2]["name"])
print(site_request["response"][3]["instanceTenantId"])
print(site_request["response"][3]["name"])

