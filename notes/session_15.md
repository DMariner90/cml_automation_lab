# 📘 Session 15 – Oct 05 2025  
**Topic:** YAML, JSON & Data Conversion  
**Milestone:** 2 – Python for Network Automation  

---

## 🧠 What I Learned
- How to read/write **JSON** with `json.load()` / `json.dump()`.
- How to parse **nested JSON** similar to Cisco API responses.
- How to read/write **YAML** with `PyYAML`.
- How to **convert JSON ⇄ YAML** (common in Ansible & CML).
- Built a challenge + stretch lab turning a YAML inventory into JSON reports.

---

## 💻 Commands & Scripts Practiced
```bash
python3 json_basics.py                 # write/read JSON
python3 parse_nested_json.py           # nested API parsing
python3 yaml_basics.py                 # read/write YAML
python3 convert_json_yaml.py           # convert JSON⇄YAML
python3 challenge_yaml_to_json.py      # filter IOS-XE devices
python3 stretch_site_summary.py        # site roll-up summary
