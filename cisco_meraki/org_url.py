import requests
from rich import print


meraki_key = "a8a49bd8da5dbb6f8f5dcca0a2c9d0aeba340049"
org_url = "https://api.meraki.com/api/v1/organizations"


headers = {
        "Authorization": f"Bearer {meraki_key}"
}

api_response = requests.get(url=org_url, headers=headers).json()
print(api_response)
