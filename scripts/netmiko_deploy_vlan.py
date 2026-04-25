"""
Basic Netmiko script to configure VLANs and VLAN NAME

Step 1.
Define a list of switches with their IP addresses and login details.

Step 2.
Use ConnectHandler() to open an SSH session to each switch.

Step 3.
Run send_config_set() to create the new VLAN and set its name.

Step 4.
Run send_command() to verify the VLAN with show vlan brief.

Step 5.
Verify with show commands

Step 6.
Use disconnect() to close the session.


"""

from netmiko import ConnectHandler

# List of devices with login details
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.10",
        "username": "admin",
        "password": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.11",
        "username": "admin",
        "password": "cisco",
    },
]

# Commands to collect information
commands = [
    "show version | include Version",
    "show ip interface brief",
    "show vlan brief",
]

# Loop through each device in the list
for device in devices:
    try:
        # Try to connect
        connection = ConnectHandler(**device)

        # Check session
        if connection.is_alive():
            print(f"\nConnected to {device['ip']}")

            # Build device-specific config
            config_commands = [f"hostname {device['hostname']}"]

            # Push configuration
            connection.send_config_set(config_commands)

            # Verify the result
            output = connection.send_command("show running-config | include hostname")
            print(f"Verification on {device['ip']}:\n{output}")
        else:
            print(f"Session to {device['ip']} not alive")

    except Exception as e:
        # Handle connection or command errors
        print(f"[ERROR] Could not connect to {device['ip']}: {e}")

    finally:
        # Always attempt to disconnect if connected
        try:
            connection.disconnect()
        except:
            pass
