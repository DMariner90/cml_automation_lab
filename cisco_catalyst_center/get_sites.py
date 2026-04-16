import requests
from rich import print

authentication_url = "https//10.10.10.85/dna/system/api/v1/auth/token"
sites_url = "https://10.10.10.85/dna/system//dna/intent/api/v1/site"
username = "administrator"
password = "Cisco1234!"

auth_request = requests.post(url=authentication_url, auth=(username, password), verify=False).json()
auth_token = auth_request["Token"]


headers = {
	"x-auth-token": "auth_token"
	"Accept": "application/json"
}

site_request = requests.get(url=sites_url, headers=headers, verify=False).json()
print(site_request)
#print(site_request["response"])
#print(site_request["response"[0])

