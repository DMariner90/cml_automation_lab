import requests
from getpass import getpass
import urllib3
import json
import yaml
import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.229.1.11/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept": "application/yang-data+json"}

username = input("Enter Username: ")
password = getpass("Enter Password: ")

response = requests.get(url, headers=headers, auth=(username, password), verify=False)
print("Status:", response.status_code)

# --- Parse JSON from RESTCONF response ---
data = response.json()

# --- Convert JSON -> YAML and print to screen ---
yaml_output = yaml.dump(data, sort_keys=False)
print(yaml_output)
