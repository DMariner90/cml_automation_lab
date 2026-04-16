# Milestone 4 – Session 2: NETCONF / RESTCONF Lab Bring-Up

This session automates the creation of a minimal CML topology from a YAML blueprint.

**Lab Name:** m4_2_netconf_lab1  
**Devices:** 1 × CSR1000v  
**Purpose:** Validate API-based lab creation, startup configuration, and NETCONF/RESTCONF reachability.

### Files
| Path | Description |
|------|--------------|
| `labs/m4_2_netconf_lab1.yaml` | YAML blueprint with metadata and topology definition |
| `scripts/create_lab_m4_2.py` | Python script to build/start the lab |
| `results/` | Folder for captured outputs (show commands, RESTCONF, NETCONF, etc.) |

### Run the lab
```bash
python3 scripts/create_lab_m4_2.py
