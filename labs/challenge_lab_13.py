"""
🧪 Challenge Lab where you combine all three in one exercise:

Use a list to hold device names.

Build a dict mapping each device to an IP.

Use a set to check if required VLANs are missing on a switch.

"""

# List of devices for the challenge lab
devices = ["R1", "R2", "SW1", "SW2", "FW1"]

# Dict of device IP mappings
device_ips = {
    "R1" : "10.0.0.1",
    "R2" : "10.0.0.2",
    "SW1" : "10.0.0.3",
    "SW2" : "10.0.0.4",
    "FW1" : "10.0.0.4"
}

# Set of required VLANs
required_vlans = {10, 20, 30, 40}

# Set of conifured VLANs on switch 1
configured_vlan_sw1 = {10, 20, 30}

# Print the device inventory list
print(f"Device Inventory: {devices}")

# Print the dictionary of devices
print("Device to IP mapping:", device_ips)

# Print the missing VLAN on switch 1
missing_vlan = required_vlans.difference(configured_vlan_sw1)
print(f"Missing VLAN on Switch 1: {missing_vlan}")