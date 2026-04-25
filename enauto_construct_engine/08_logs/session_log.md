## Session 1 - RESTCONF Interfaces

Date: 2026-04-24

Objective:
- Build CML Cat8000v RESTCONF lab from scratch.
- Validate WSL to CML connectivity.
- Use Python requests to retrieve interface data.

Built:
- enauto_construct_engine/01_drills/restconf/restconf_interfaces_day01.py

Errors / friction:
- External connector initially used NAT/virbr0.
- Router was not reachable from WSL until bridge0 was used.
- SSH known_hosts warning after CML rebuild.

ENAUTO links:
- RESTCONF
- API authentication
- JSON parsing
- Constructing Python scripts

Confidence:
- /10

Next:
- Rebuild RESTCONF interface script from memory.