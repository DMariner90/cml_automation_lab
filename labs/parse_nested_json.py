import json  # For handling JSON data

# Simulated API response from a network device
api_response = {
    "device": {
        "hostname": "edge-switch-1",
        "interfaces": [
            {"name": "Gig0/0", "status": "up", "ip": "10.10.10.1"},
            {"name": "Gig0/1", "status": "down", "ip": "10.10.20.1"},
            {"name": "Gig0/2", "status": "up", "ip": "10.10.30.1"}
        ],
        "system": {"os": "IOS-XE", "version": "17.9.3"}
    }
}

# Convert Python dict → JSON string (mimicking an API payload)
json_data = json.dumps(api_response, indent=4)
print("🔹 Raw JSON Output:\n", json_data)

# Parse JSON string → Python dict
parsed = json.loads(json_data)

# --- Extract key values ---
print("\n🔹 Device Hostname:", parsed["device"]["hostname"])  # Single key access
print("🔹 OS Version:", parsed["device"]["system"]["version"])  # Nested access

# --- Loop through a list of interfaces ---
print("\n🔹 Interface Summary:")
for iface in parsed["device"]["interfaces"]:
    # Iterate each dict in the list and format output
    print(f"  {iface['name']:10} | Status: {iface['status']:4} | IP: {iface['ip']}")

# --- Conditional logic example ---
# Show only interfaces that are up
print("\n🔹 Interfaces that are UP:")
for iface in parsed["device"]["interfaces"]:
    if iface["status"] == "up":
        print(f"  ✅ {iface['name']} is UP with IP {iface['ip']}")
