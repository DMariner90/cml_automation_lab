# 📘 Session 16 – Oct 06, 2025
**Topic:** NX-OS Always-On via NX-API (HTTPS JSON)
**Milestone:** 2 – Python for Network Automation

---

## 🧠 What I Learned
- How to call **NX-API** over HTTPS (`POST /ins`) with JSON payloads.
- Auth with `requests` and parse **nested JSON** responses from NX-OS.
- Convert interface data to **filtered reports** and export to **JSON/CSV**.
- Why NX-API is a practical alternative to RESTCONF on the Always-On switch.

---

## 💻 Commands & Scripts Practiced
```bash
python3 scripts/nxos_get_hostname.py        # show hostname via NX-API
python3 scripts/nxos_show_interfaces.py     # show interface brief -> parsed
python3 scripts/nxos_challenge_export.py    # filter UP+IP -> JSON & CSV

🔍 What / Why / How (Key Steps)

What: Send a JSON body with a CLI string (e.g., show interface brief) to /ins.

Why: NX-API returns structured JSON suitable for automation/reporting.

How:

Headers: {"Content-Type": "application/json"}

Auth: requests.post(url, auth=(USER, PASS), json=payload, verify=False)

Parse path: ins_api → outputs → output → body → TABLE_* → ROW_*

Filter and export using json.dump() and csv.DictWriter.

🔎 Review / Recap

Practiced HTTP auth, robust error handling, JSON parsing, and file exports.

Learned the common JSON structure used by NX-API responses.

Produced tangible outputs: labs/nxos_up_interfaces.json and .csv.

⚡ Troubleshooting
Symptom	Likely Cause	Fix
401 Unauthorized	Wrong/expired creds	Check Quick Access creds and re-export NXOS_USER/NXOS_PASS.
SSL warnings/errors	Lab certs	Use verify=False (lab only). In prod, use a CA bundle.
KeyError / missing keys	Command/table names vary	print(resp.text[:1000]) and inspect TABLE_* / ROW_* keys.
Empty/odd responses	Rate-limit or shared box	Wait 1–2 min and try again.