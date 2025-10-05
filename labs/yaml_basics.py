import yaml  # third-party: PyYAML

# Python dict that could be a tiny CML-like topology
lab_topology = {
    "lab_name": "CML Demo",
    "nodes": [
        {"name": "R1", "os": "IOS-XE", "ip": "10.0.0.1"},
        {"name": "R2", "os": "IOS-XE", "ip": "10.0.0.2"},
    ]
}

# --- Write YAML (human-friendly) ---
with open("topology.yaml", "w") as f:
    yaml.dump(lab_topology, f, sort_keys=False)  # keep key order readable

print("✅ Wrote topology.yaml")

# --- Read YAML back into Python ---
with open("topology.yaml") as f:
    data = yaml.safe_load(f)  # safe_load parses YAML → Python objects

print("✅ Loaded YAML:", data)
print("🔹 First node name:", data["nodes"][0]["name"])
