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

check_auth = api_session.post(url=authentication_url, data=payload, verify=False)
print(check_auth)

device_siteid_url = "https://10.10.20.90/dataservice/device?site-id=101"

list_of_devices = api_session.get(url=device_siteid_url, verify=False).json()
print(list_of_devices)

        
