# 📘 Session 13 – Python Collections (Lists, Dicts, Sets)  
**Date:** Sep 22, 2025  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- **Lists** store ordered device inventories.  
- **Dicts** map devices to attributes (IP, role) like API responses.  
- **Sets** make VLAN/state comparisons easy with `.difference()` and `.intersection()`.  
- Combining collections lets you build **inventory + compliance checks** just like in automation workflows.  

---

## �� Code & Concepts Practiced  

### Lists  
```python
devices = ["R1", "SW1", "R2", "FW1"]
devices.append("SW2")        # add item
print(devices[0:2])          # slicing
for dev in devices:          # iteration
    print(dev)
Dicts
python
Copy code
device_ips = {"R1": "10.0.0.1", "SW1": "10.0.0.10"}
device_ips["SW2"] = "10.0.0.11"    # add key:value
for name, ip in device_ips.items(): 
    print(name, ip)
Sets
python
Copy code
required = {10, 20, 30, 40}
configured = {10, 20, 30}
missing = required.difference(configured)
print("Missing VLANs:", missing)
🔎 Review / Recap
Lists = ordered inventories.

Dicts = structured attributes/configs.

Sets = compliance/state checks.

Real-world automation always blends these.

⚡ Troubleshooting
KeyError → access non-existent dict key. Fix: use dict.get("key").

Unhashable type → tried to put list/dict inside a set. Fix: only use hashable (immutable) types.

Unexpected VLANs → wrong set operation. Fix: check .difference() vs .intersection().

🧪 Challenge Lab
List → ["R1","R2","SW1","SW2","FW1"]

Dict → map devices to IPs.

Set → compare required vs configured VLANs.

✅ Expected Result:

yaml
Copy code
Device Inventory: [...]
Device to IP Mapping: {...}
Missing VLANs on SW1: {40}
🏋️ Stretch Challenge
Built a Network Inventory System:

List = devices.

Dict = nested IP + role mapping.

Sets = VLAN compliance check.

For loop = clean inventory report.

✅ Expected Result:

cpp
Copy code
SW1 (switch) - 10.0.0.3 | Missing VLANs: {40}
SW2 (switch) - 10.0.0.4 | Missing VLANs: {30}
🧠 Self-Check + ✅ Answers
How do you append a device to a list? → devices.append("SW2").

How do you loop through dict keys & values? → for k, v in dict.items():.

What does .difference() do? → Shows items in one set but not the other.

What’s the advantage of dicts over lists? → Faster lookups by key.

Can sets contain duplicates? → No, they automatically remove duplicates.

📚 Glossary
List → Ordered, indexed collection.

Dict → Key:value mapping, like JSON.

Set → Unique, unordered collection for comparisons.

💭 Last Thoughts
Collections are everywhere in automation.

Lists = inventories.

Dicts = configs and API responses.

Sets = compliance checks.
Being able to combine them makes scripts far more powerful and realistic.
