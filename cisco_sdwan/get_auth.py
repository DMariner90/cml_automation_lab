import requests
import urllib3
from rich import print

urllib3.disable_warnings()

payload = {
        "j_username": "admin",
        "j_password": "C1sco12345"
}


authentication_url = "https://10.10.20.90/j_security_check"

api_session = requests.session()

authentication_request = api_session.post(url=authentication_url, data=payload, verify=False)
print(authentication_request)

