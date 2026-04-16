import netmiko
from netmiko import ConnectHandler

# Device connection details
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.10",
    "username": "admin",
    "password": "cisco"
}

# Open the SSH connection
connection = ConnectHandler(**device)

# Run a simple operational command
output = connection.send_command("show ip interface brief")

# Print the result
print(output)

# Close the session
connection.disconnect()