import json
import yaml

# load routers.yml file
with open("labs/routers.yaml", "r") as f:
    inventory = yaml.safe_load(f)
    #print(inventory)

routers = inventory.get("routers", [])
#print(routers)

iosxe_devices = []
for device in routers:
    if str(device.get("os", "")).strip().upper() == "IOS-XE":
        iosxe_devices.append({
            "name": device.get("name"),
            "IP": device.get("ip"),
            "Site": device.get("site")
        })
# print(iosxe_devices)

export_payload = {
    "count" : len(iosxe_devices),
    "devices" : iosxe_devices
}

#print(export_payload)

with open("labs/routers_iosxe.json", "w") as output:
    json.dump(export_payload, output, indent=2)

print(f"Exported {export_payload['count']} IOS-XE routers -> labs/routers_iosxe.json")


site_rollup = {}
for device in routers:
    site = device.get("site", "UNKNOWN")
    site_rollup.setdefault(site, {"total": 0, "ios_xe": 0})
    site_rollup[site]["total"] += 1
    if str(device.get("os", "")).upper() == "IOS-XE":
        site_rollup[site]["ios_xe"] += 1
print(f"Site rollup: {site_rollup[site]}")
    