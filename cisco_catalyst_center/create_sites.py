import requests
import urllib3
from rich import print

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTHENTICATION_URL = "https://10.10.20.85/dna/system/api/v1/auth/token"
CREATE_SITES_URL = "https://10.10.20.85/dna/intent/api/v1/site"
USERNAME = "administrator"
PASSWORD = "Cisco1234!"

authentication_request = requests.post(url=AUTHENTICATION_URL, auth=(USERNAME, PASSWORD), verify=False).json()
auth_token = authentication_request["Token"]


HEADERS = {
	"x-auth-token": auth_token,
	"Accept": "application/json",
	"Content-Type": "application/json"
}

PAYLOAD = {
	"type": "area",
	"site":{
	  "area":{
		  "name": "England",
		  "parentName": "Global"
		}
	},
	"type": "area",
	"site":{
		"area":{
			"name": "Spain",
			"parentName": "Global"
		}
	},
	"type": "area",
	"site": {
		"area": {
			"name": "Ireland",
			"parentName": "Global"
		}
	}
}

create_site_request = requests.post(url=CREATE_SITES_URL, headers=HEADERS, json=PAYLOAD, verify=False)
print(create_site_request.text)

