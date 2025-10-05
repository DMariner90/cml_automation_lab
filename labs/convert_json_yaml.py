import json, yaml

# Start from a JSON file created earlier (device_info.json).
# If you don't have it, quickly generate it:
# json.dump({"hostname": "core-router", "ip": "10.229.1.1"}, open("device_info.json","w"))

# --- JSON → YAML ---
with open("device_info.json") as f:
    json_data = json.load(f)             # JSON → Python dict

with open("device_info_converted.yaml", "w") as f:
    yaml.dump(json_data, f, sort_keys=False)

print("✅ Converted JSON → YAML → device_info_converted.yaml")

# --- YAML → JSON (using topology.yaml from previous lab) ---
with open("topology.yaml") as f:
    topo = yaml.safe_load(f)             # YAML → Python dict

with open("topology_converted.json", "w") as f:
    json.dump(topo, f, indent=2)

print("✅ Converted YAML → JSON → topology_converted.json")
