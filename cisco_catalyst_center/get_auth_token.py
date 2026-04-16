import requests

authentication_url = "https//10.10.10.85/dna/system/api/v1/auth/token"
username = "administrator"
password = "Cisco1234!"

auth_request = requests.post(url=authentication_url, auth=(username, password), verify=False)
print (auth_request)