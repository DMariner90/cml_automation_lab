import requests
from getpass import getpass
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.229.1.91/restconf/data/ietf-interfaces:interfaces/interface=Loopback10"
headers = {"Accept": "application/yang-data+json"}

username = getpass("Enter Username: ")
password = getpass("Enter Password: ")

resp = requests.get(url, headers=headers, auth=(username, password), verify=False)
print("Status:", resp.status_code)
print(resp.text)
