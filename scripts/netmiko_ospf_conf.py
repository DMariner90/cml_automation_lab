"""
Basic Netmiko script to configure OSPF on the listed devices

Step 1.
Define the device inventory with IP addresses and login details.

Step 2.
Establish SSH sessions with Netmiko.

Step 3.
Push the routing configuration commands (for example, enable OSPF or BGP).

Step 4.
Run verification commands such as show ip ospf neighbor or show ip route.

Step 5.
Parse the results or save them for later review.

Step 6.
Disconnect the sessions cleanly.


"""

from netmiko import ConnectHandler

# Define router's parameters
DEVICE_IP = "10.229.1.11"  # IP address of the router
DEVICE_USERNAME = "netauto"  # username for accessing the router
DEVICE_PASSWORD = "cisco123!"  # password for accessing the router
DEVICE_TYPE = "cisco_xe"  # device type

# Using Netmiko ConnectHandler class to initiate connection to device
router = ConnectHandler(
    host=DEVICE_IP,
    username=DEVICE_USERNAME,
    password=DEVICE_PASSWORD,
    device_type=DEVICE_TYPE,
)


ip_protocols = router.send_command_timing("show ip pro")
print(ip_protocols)

ospf_routing = ["router ospf 10", "network 10.100.0.4 0.0.0.0 area 0"]
router.send_config_set(ospf_routing)
