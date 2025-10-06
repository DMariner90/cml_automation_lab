import json  # Import built-in JSON module

# Define a simple Python dictionary — like a device API response
device_info = {
    "hostname": "core-router",
    "ip": "10.229.1.1",
    "os": "IOS-XE",
    "version": "17.9.3",
}

# --- Write JSON file ---
# 'w' means write mode — this will create (or overwrite) a file
with open("device_info.json", "w") as f:
    json.dump(device_info, f, indent=4)  # indent=4 formats the JSON nicely

# --- Read JSON file ---
with open("device_info.json") as f:
    data = json.load(f)  # loads() converts JSON → Python dictionary
    print("✅ Loaded JSON Data:", data)
