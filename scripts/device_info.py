
device_name = "router1"
device_ip = "10.10.10.10"
port = 22
is_active = True

supported_devices = ["router", "switch", "firewall"]

credentials = {"username" : "david", "password" : "test"}

print(f"Device Name: {device_name}")
print(f"Device IP: {device_ip}")
print(f"Device Port: {port}")
print(f"Device is active: {is_active}")
print()
print(f"Supported Device Types: {supported_devices}")
print()
print(f"User Credentials: {credentials}")

username = input("What is your name? ")
print(f"Hello {username}, welcome to the automation lab!")
