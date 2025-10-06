import yaml

# load routers.yml file
with open("labs/routers.yaml", "r") as f:
    inventory = yaml.safe_load(f)
    # print(inventory)

routers = inventory.get("routers", [])
# print(routers)

switches = inventory.get("switches", [])
# print(switches)

iosxe_devices = []
for device in routers + switches:
    if str(device.get("os", "")).strip().upper() == "IOS-XE":
        iosxe_devices.append(
            {
                "name": device.get("name"),
                "IP": device.get("ip"),
                "Site": device.get("site"),
            }
        )
# print(iosxe_devices)

export_payload = {"count": len(iosxe_devices), "devices": iosxe_devices}

print(export_payload)
