🧾 Session 17 Notes Summary

📄 Location: notes/session_17.md

# 📘 Session 17 – Oct 6, 2025 | Topic: Mini Network API Tool | Milestone 2 – Capstone

---

## 🧠 What I Learned
- Combined all Python fundamentals into a functional automation workflow.
- Practiced live RESTCONF calls with `requests`.
- Parsed JSON API responses and saved outputs to YAML.
- Implemented proper exception handling and mock fallback.
- This structure forms the baseline of tools like Ansible, Nornir, and pyATS.

---

## 💻 Commands & Code Practiced

```python
import requests, json, yaml  # Import required libraries

device = {  # Define RESTCONF device parameters
    "host": "sandbox-iosxe-recomm-1.cisco.com",
    "port": 443,
    "username": "developer",
    "password": "C1sco12345"
}

url = f"https://{device['host']}:{device['port']}/restconf/data/ietf-interfaces:interfaces"
headers = {"Accept": "application/yang-data+json"}

try:
    resp = requests.get(url, headers=headers, auth=(device["username"], device["password"]), verify=False)
    resp.raise_for_status()
    data = resp.json()
except requests.exceptions.RequestException as err:
    print(f"❌ API request failed: {err}")
    data = {"ietf-interfaces:interfaces": {"interface": [{"name": "Loopback0", "enabled": True}]}}


Practiced safe dictionary lookups and key validation.

Wrote structured YAML outputs with yaml.dump().

🔍 Review / Recap

Full RESTCONF → JSON → YAML workflow mastered.

Demonstrated error handling for production safety.

Learned importance of “mock” logic for testing offline.

⚡ Troubleshooting
Symptom	Root Cause	Fix
401 Unauthorized	Retired sandbox / wrong credentials	Use mock data or NX-API
SSL Error	Self-signed lab certificate	Add verify=False
Empty data	Wrong JSON key	Use print(data.keys()) to debug
🧪 Challenge Lab

Goal: Extend script to pull IPv4 info and filter for enabled interfaces.
Expected Output:

🧩 Found 3 enabled interfaces:
 - GigabitEthernet1 (10.10.20.48)
 - Loopback0 (172.16.1.1)

🧭 Challenge Walkthrough

Added second RESTCONF endpoint /restconf/data/ietf-ip:interfaces-state.

Merged JSON structures and filtered by enabled=True.

Saved results in labs/enabled_interfaces.yaml.

💭 Last Thoughts

Milestone 2 showed how Python connects to real devices through APIs.
Next step: build and automate your own lab in CML.