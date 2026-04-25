import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

AUTHENTICATION_URL = "https://10.10.20.85/dna/system/api/v1/auth/token"
USERNAME = "administrator"
PASSWORD = "Cisco1234!"

authentication_request = requests.post(
    url=AUTHENTICATION_URL,
    auth=(USERNAME,PASSWORD),
    verify=False
).json()
print(authentication_request["Token"])
