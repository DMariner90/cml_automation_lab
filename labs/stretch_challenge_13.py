"""
Stretch Challenge

Build a mini inventory/reporting system that:

Stores devices in a list: ["R1", "R2", "SW1", "SW2", "FW1"].

Uses a dict to map each device to both an IP address and a role (router, switch, firewall).

Example: {"R1": {"ip": "10.0.0.1", "role": "router"}}.

Uses sets to compare required VLANs {10, 20, 30, 40} against configured VLANs for each switch (SW1, SW2).

Example: SW1 has {10, 20, 30}, SW2 has {10, 20, 40}.

Prints a clean report:

Device name, role, and IP.

For switches → list missing VLANs.


"""

# Device inventory
devices = ["R1", "R2", "SW1", "SW2", "FW1"]

# Dictionary for mappings of devices
device_mappings = {
    "R1" : {"ip" : "10.0.0.1", "Role" : "Router"},
    "R2" : {"ip" : "10.0.0.2", "Role" : "Router"},
    "SW1" : {"ip" : "10.0.0.3", "Role" : "Switch"},
    "SW2" : {"ip" : "10.0.0.4", "Role" : "Switch"},
    "FW1" : {"ip" : "10.0.0.5", "Role" : "Firewall"}
}

# Set of VLANs required and configured on the switches
required_vlans = {10, 20, 30, 40}
configured_vlan = {
    "SW1" : {10, 20 ,30},
    "SW2" : {10,20,40}
}
    

print("Inventory Report:")

for device in devices:
    ip = device_mappings[device]["ip"]          # Grab IP from nested dictionary
    role = device_mappings[device]["Role"]      # Grab Role from nested dictionary
    
    if role == "Switch":
        # Compare VLAN sets: required vs. configured - missing
        missing_vlan = required_vlans.difference(configured_vlan[device])
        print(f"{device} ({role}) - ({ip} | Missing VLANs: {missing_vlan})")
    else:
        # For non-switches, no vlan check required
        print(f"{device} ({role}) - ({ip})")
    

    