#!/usr/bin/env python3

"""
NETCONF TEMPLATE SCRIPT
-----------------------
Generic, heavily-commented template for performing NETCONF operations against
IOS XE / Cat8000v / CSR1000v devices (e.g. in your CML lab).

Supported operations in this template:
- get        : generic <get>, usually for operational/state data
- get_config : <get-config>, typically from "running" datastore
- edit_config: <edit-config> to push configuration

How to use:
1. Install ncclient:  pip install ncclient
2. Populate DEVICES with your lab nodes.
3. Choose OPERATION = "get" / "get_config" / "edit_config".
4. Update FILTER_XML and/or CONFIG_XML as needed for your task.
"""

from getpass import getpass
from ncclient import manager
from ncclient.operations import RPCError

# ---------------------------------------------------------------------------
# DEVICE INVENTORY
# Add your lab devices here as dictionaries.
#   host: IP or hostname
#   port: NETCONF port (default for IOS XE is usually 830)
# ---------------------------------------------------------------------------
DEVICES = [
    # Example:
    # {"name": "R1", "host": "10.229.1.21", "port": 830},
    # {"name": "R2", "host": "10.229.1.22", "port": 830},
]

# ---------------------------------------------------------------------------
# NETCONF OPERATION
# Choose ONE of:
#   "get", "get_config", "edit_config"
# ---------------------------------------------------------------------------
OPERATION = "get"  # Change as needed


# ---------------------------------------------------------------------------
# XML FILTER (for "get" or "get_config")
# Optional: limits the data returned.
# Set to None for no filter (not always recommended).
#
# Example filter (get all interfaces using ietf-interfaces):
# FILTER_XML = """
# <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
#   </interfaces>
# </filter>
# """
# ---------------------------------------------------------------------------
FILTER_XML = None  # or replace with an XML string as shown above


# ---------------------------------------------------------------------------
# CONFIG PAYLOAD (for "edit_config")
# Only used when OPERATION == "edit_config".
# This should be an XML snippet representing the desired configuration
# in the target datastore (usually "running").
#
# Example (create Loopback 99 via native model):
# CONFIG_XML = """
# <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#     <interface>
#       <Loopback>
#         <name>99</name>
#         <ip>
#           <address>
#             <primary>
#               <address>99.99.99.99</address>
#               <mask>255.255.255.255</mask>
#             </primary>
#           </address>
#         </ip>
#       </Loopback>
#     </interface>
#   </native>
# </config>
# """
# ---------------------------------------------------------------------------
CONFIG_XML = None  # Replace with your <config> XML when doing edit_config


# ---------------------------------------------------------------------------
# NETCONF CONNECTION OPTIONS / CAPABILITIES
# hostkey_verify=False is typical for lab work with self-signed keys.
# ---------------------------------------------------------------------------
def netconf_connect(host, port, username, password):
    """
    Open a NETCONF session to the given device and return the manager object.
    """
    return manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False,  # Do not verify host key (lab-friendly)
        allow_agent=False,  # Don't use SSH agent
        look_for_keys=False,  # Don't use local SSH keys
        timeout=30,  # Session timeout in seconds
    )


def main():
    print("=== NETCONF TEMPLATE SCRIPT ===")
    print(f"Operation: {OPERATION}")
    print(f"Devices configured: {len(DEVICES)}\n")

    if not DEVICES:
        print("No devices defined in DEVICES list. Add at least one device.")
        return

    username = input("Enter NETCONF username: ")
    password = getpass("Enter NETCONF password: ")

    for device in DEVICES:
        name = device["name"]
        host = device["host"]
        port = device.get("port", 830)  # Default to 830 if not specified

        print(f"\n--- {name} ({host}:{port}) ---")

        try:
            # Establish NETCONF session
            with netconf_connect(host, port, username, password) as m:
                print("NETCONF session established.")

                # -------------------------
                # OPERATION: GET
                # -------------------------
                if OPERATION == "get":
                    if FILTER_XML:
                        print("Sending <get> with filter...")
                        reply = m.get(FILTER_XML)
                    else:
                        print("Sending <get> without filter...")
                        reply = m.get()

                # -------------------------
                # OPERATION: GET-CONFIG
                # -------------------------
                elif OPERATION == "get_config":
                    if FILTER_XML:
                        print('Sending <get-config> from "running" with filter...')
                        reply = m.get_config(source="running", filter=FILTER_XML)
                    else:
                        print('Sending <get-config> from "running" without filter...')
                        reply = m.get_config(source="running")

                # -------------------------
                # OPERATION: EDIT-CONFIG
                # -------------------------
                elif OPERATION == "edit_config":
                    if not CONFIG_XML:
                        print("No CONFIG_XML defined for edit_config. Skipping.")
                        continue

                    print('Sending <edit-config> to "running"...')
                    reply = m.edit_config(target="running", config=CONFIG_XML)

                else:
                    print(f"Unsupported OPERATION: {OPERATION}")
                    continue

                # If we get here, we have a reply from the device
                print("\nNETCONF RPC Reply:")
                # .xml gives a pretty-printed XML string
                print(reply.xml)

                # Save reply to a file for later inspection
                filename = f"{name.lower()}_netconf_{OPERATION}.xml"
                with open(filename, "w") as f:
                    f.write(reply.xml)
                print(f"Saved reply to {filename}")

        except RPCError as rpc_err:
            print(f"NETCONF RPC error on {name}: {rpc_err}")
        except Exception as e:
            print(f"General error on {name}: {e}")


if __name__ == "__main__":
    main()
