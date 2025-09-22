# ------ Lab 1: Lists for Device Inventories -----

# Create a list of devices
devices = ["R1", "SW1", "R2", "FW1"]

# Print the whole list
print("All Devices: ", devices)

# Access by list index (0-based, so devices[0] = first item
print("First Device: ", devices[0])

# Slice list of devices (from index[0] up to, but not including 2)
print("First two devices: ", devices[0:2])

# Add a new device to the list
devices.append("SW2")
print("Updated devices: ", devices)

# Iterate through the entire list
for device in devices:
    print(f"Connecting to {device}...")

print("---------- BREAK LINE LAB - END OF 1 ----------")


# ------ Lab 2: Dictionaries for Device Attributes -----

# Create a dictionary mapping device names to IPs
device_ips = {
    "R1": "10.0.0.1",
    "R2": "10.0.0.2",
    "SW1": "10.0.0.10",
    "FW1": "10.0.0.254",
}

# print the whole dictionary
print("Device IP mapping: ", device_ips)

# Access a value by key
print("R1's IP is:", device_ips["R1"])

# Add a new device
device_ips["SW2"] = "10.0.0.11"
print("Updated mappings:", device_ips)

# Iterate through keys and values
for name, ip in device_ips.items():
    print(f"Device {name} has IP {ip}")

print("---------- BREAK LINE - END OF LAB 2 ----------")

# ----- Lab 3: Sets for VLAN Comparison -----

# Required VLANs VS. Configured VLANs
required_vlans = {10, 20, 30, 40}
configured_vlans = {10, 20, 30}

print("Required VLANs:", required_vlans)
print("Configured VLANs:", configured_vlans)

# Fine missing VLANs
missing_vlans = required_vlans.difference(configured_vlans)
print("Missing VLANs:", missing_vlans)

# Find common VLANs
common_vlans = required_vlans.intersection(configured_vlans)
print("Common VLANs:", common_vlans)

# Add a VLAN to the set
configured_vlans.add(40)
print("Updated Configured VLANs:", configured_vlans)

print("---------- BREAK LINE - END OF LAB 3 ----------")
