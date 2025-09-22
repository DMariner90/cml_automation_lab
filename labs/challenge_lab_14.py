# Challenge Lab: REad Inventory & Log connections

"""
Reads the list of devices from devices.txt.

Loops through them and simulates connecting.

Writes results into labs/connection_log.txt.

Appends results if run multiple times.

"""

# Read in devices from devices.txt
with open("labs/devices.txt", "r") as read_file:
    devices = read_file.read().splitlines()               # Splitlines() removes new lines

print(f"Devices loaded from file... {devices}")

# Append simulated connection results to log

with open("labs/connection_log.txt", "a") as appended_logs:
    for dev in devices:
        # simulate a "SUCCESS" connection for all devices
        appended_logs.write(f"Connecting to {dev}... SUCCESS\n")

print("Connection results appended to labs/connections_log.txt")
