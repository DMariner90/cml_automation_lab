from netmiko import ConnectHandler

# Define router's parameters
device_ip = "172.16.10.1"  # IP address of the router
device_username = "admin"  # username for accessing the router
device_password = "1234QWer"  # password for accessing the router
device_type = "cisco_xe"  # device type

# Using Netmiko ConnectHandler class to initiate connection to device
router = ConnectHandler(
    host=device_ip,
    username=device_username,
    password=device_password,
    device_type=device_type,
)


def check_network_in_routing_table(target_network):

    # Retrieve routing table using TextFSM if available
    routes = router.send_command("show ip route", use_textfsm=True)

    if not routes:
        print("Could not parse routing table with TextFSM, showing raw output instead:")
        raw_output = router.send_command("show ip route")
        print(raw_output)
        router.disconnect()
        return False

    # Check if target network is in the table
    found = any(route.get("network") == target_network for route in routes)

    if found:
        print(f"Network {target_network} is present in the routing table.")
    else:
        print(f"Network {target_network} is NOT found in the routing table.")

    router.disconnect()
    return found
