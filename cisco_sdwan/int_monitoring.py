import requests
import urllib3
from rich import print

urllib3.disable_warnings()

vmanage_ip = "10.10.20.90"
int_monitoring_device_ip = "10.10.1.3"

auth_payload = {"j_username": "admin", "j_password": "C1sco12345"}

j_sec_auth_url = f"https://{vmanage_ip}/j_security_check"
xsrf_token_url = f"https://{vmanage_ip}/dataservice/client/token"
list_devices_url = f"https://{vmanage_ip}/dataservice/device"
monitoring_device_interface_url = f"https://{vmanage_ip}/dataservice/device/interface?deviceId={int_monitoring_device_ip}"


headers = {
    "Content-Type": "application/json",
    "X-XSRF-TOKEN": "xsrf_token"
}

session = requests.session()

auth_response = session.post(url=j_sec_auth_url, data=auth_payload, verify=False)
print(auth_response)

xsrf_token_response = session.get(url=xsrf_token_url, verify=False)
xsrf_token = xsrf_token_response.text

devices_url_response = session.get(url=list_devices_url, verify=False).json()
#print(devices_url_response["data"])

for device in devices_url_response["data"]:
        device_id = device['deviceId']
        hostname = device['host-name']
        device_type = device['device-type']
        site_id = device['site-id']
        print("\n============")
        print(f"DEVICE ID:{device_id}")
        print(f"HOSTNAME:{hostname}")
        print(f"SITE ID:{site_id}")
        print(f"DEVICE TYPE: {device_type}")
        print("\n============")

device_int_monitoring = session.get(url=monitoring_device_interface_url, verify=False).json()
#print(device_int_monitoring["data"])

for interface in device_int_monitoring['data']:
    interface_name = interface['ifname']
    print("\n============")
    print(f"INTERFACE NAME: {interface_name}")
    
    
    
    
    

