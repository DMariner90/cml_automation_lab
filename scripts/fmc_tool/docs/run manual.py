# FMC Tool — Run Manual

This manual explains what **fmc_tool** does, how to run it, how the parts fit together, and how to troubleshoot common issues.  
It is written for someone who **does not need to be a programmer** to use it.

---

## What this tool does

**fmc_tool** is a small interactive command-line tool for Cisco **Firepower Management Center (FMC)**.

In one run, it:

1. Logs into FMC (you type username and password).
2. Shows you a list of FMC **domains** and asks you to pick one.
3. Creates **one run folder** under `outputs/` to store everything from that session.
4. Lets you pick a **task** to run (for example, “get rules”).
5. Saves the results into the same run folder in **YAML** (default) or **JSON** (optional).
6. Lets you run **more tasks** in the same run folder if you want.

---

## Requirements (what you need installed)

### 1) Python virtual environment (recommended)
You are already using `.venv`, which is great.

### 2) Python packages

The tool uses:

- `requests`
- `urllib3`
- `pyyaml` (only needed if you choose YAML output, but YAML is the default so install it)

Install:

```bash
pip install requests urllib3 pyyaml
```

---

## Folder structure

Inside your repo, you have:

```
fmc_tool/
├── fmc_orchestrator.py
├── main.py
├── tasks/
│   ├── __init__.py
│   ├── get_rules.py
│   ├── get_network_objects.py
│   ├── get_interfaces.py
│   └── get_nat_policies.py
└── outputs/
    └── (created automatically)
```

**What each part is for:**

- `main.py`  
  The “front desk” of the tool. This is what you run. It handles the menus and calling tasks.

- `fmc_orchestrator.py`  
  The “engine room.” It contains shared functions used by all tasks:
  - login/authentication
  - listing/choosing domains
  - listing/choosing policies
  - listing/choosing devices
  - pagination helper
  - output folder creation
  - writing output files (YAML/JSON)
  - run logging

- `tasks/`  
  Each file is one **task**. Tasks contain the “what to query” logic and write results into the run folder.

- `outputs/`  
  Auto-created. Each run makes a new subfolder to keep outputs tidy.

---

## How to run the tool

From inside the `fmc_tool` directory:

```bash
python3 main.py
```

You will be asked:

1) **FMC username**  
2) **FMC password** (hidden as you type)

Then the menus start.

---

## What you will see when running

### Step 1 — Authenticate
You enter username/password.  
The tool requests an access token from FMC using the auth endpoint.

If auth works, the tool continues. If not, it stops and prints the error.

### Step 2 — Select a domain
It prints domains like:

```
1) Global | UUID: xxxxx
2) Lab    | UUID: yyyyy
```

You type the number.

### Step 3 — Create a run folder
After domain selection, the tool creates one folder:

```
outputs/20251214-123456__domain-Global__uuid-xxxxxxxx/
```

Everything in that run is saved there.

### Step 4 — Choose the default output format
You select:

- YAML (default, easiest to read)
- JSON

You can also override the format **per task** later.

### Step 5 — Choose a task (job)
The task menu lists tasks like:

- Get all access rules for selected/all policies
- Get all network objects
- Get interfaces for selected/all devices
- Get all NAT policies

### Step 6 — Optional: run another task in same run folder
After a task completes, you’ll be asked if you want to run another.

This keeps all related outputs grouped in the same run folder.

---

## What files are created in outputs

Each run folder contains at least:

- `run_log.yaml` (or `run_log.json` if YAML is not available)

And task outputs, for example:

- `get_network_objects.yaml`
- `get_nat_policies.yaml`
- `get_interfaces__device-FTD01.yaml`
- `get_rules__policy-Internet_Edge.yaml`

### What is the run log?

`run_log.yaml` is a chronological record of what tasks were run and with what settings, for example:

- when the run started
- which task ran
- output format
- selection notes (policy selection/device selection)

This is useful for audit/troubleshooting and for handing results to someone else.

---

## How the tool works (logic overview)

This section explains the internal logic in plain English.

### main.py (the menu controller)

`main.py` does these steps:

1. Ask user for username/password
2. Call `fmc_authenticate(...)` to get an access token
3. Call `fmc_list_domains(...)` and `select_domain(...)` to choose a domain
4. Create a run folder with `create_run_folder(...)`
5. Create a `RunContext` (run folder, domain name, domain uuid, output format)
6. Start a loop:
   - show task menu
   - run the selected task
   - ask if user wants another task
7. Exit

### fmc_orchestrator.py (shared engine)

The orchestrator provides reusable functions:

- Authentication:
  - `fmc_authenticate(username, password) -> access_token`
- Domain handling:
  - `fmc_list_domains(access_token)`
  - `select_domain(domains) -> selected_domain_dict`
- Policy handling (used by get_rules task):
  - `fmc_list_policies(access_token, domain_uuid)`
  - `select_policies(policies) -> (selected_policies, selection_note)`
- Device handling (used by get_interfaces task):
  - `fmc_list_devices(access_token, domain_uuid)`
  - `select_devices(devices) -> (selected_devices, selection_note)`
- Pagination:
  - `fmc_get_all_items(access_token, url, ...)` loops `offset/limit` until all pages are retrieved
- Outputs:
  - `create_run_folder(domain_name, domain_uuid)`
  - `write_output(ctx, file_stem, payload)` writes YAML/JSON into the run folder
  - `append_run_log(ctx, entry)` appends entries to the run log file

### tasks/ (each task file)

Each task:
- gets passed the access token + run context (`ctx`)
- makes one or more FMC API calls
- writes outputs into the run folder
- logs to `run_log.yaml`

---

## What each built-in task does

### 1) get_rules
Purpose: **Get all access rules** for selected/all access policies in the selected domain.

What it does:
1. Lists access policies in the domain
2. Lets user select all or specific policies
3. For each selected policy:
   - GETs `/accessrules` (using pagination)
   - writes one output file per policy

Output:
- One file per policy, e.g. `get_rules__policy-<POLICYNAME>.yaml`

### 2) get_network_objects
Purpose: Get all **network objects** (e.g. networks) in the selected domain.

Output:
- `get_network_objects.yaml`

### 3) get_interfaces
Purpose: Get **operational interfaces** for selected/all devices in the domain.

What it does:
1. Lists devices
2. Lets user select all or specific devices
3. For each selected device:
   - GETs interfaces endpoint
   - writes one output file per device

Output:
- `device_inventory.yaml` (snapshot of devices)
- one file per device: `get_interfaces__device-<DEVICENAME>.yaml`

### 4) get_nat_policies
Purpose: Get all **NAT policies** in the selected domain.

Output:
- `get_nat_policies.yaml`

---

## Troubleshooting

### Authentication failed (HTTP 401/403)
Common causes:
- wrong username/password
- user account does not have API permissions
- FMC is using external auth that rejects basic auth

What to do:
- confirm credentials can log into FMC UI
- confirm user has required permissions (API access)
- ensure you are targeting the correct FMC host/IP

### Connection error / timeout
Common causes:
- wrong FMC_HOST
- routing/DNS issue
- firewall blocks access
- FMC is down

What to do:
- ping FMC host (if allowed)
- check you can access FMC UI in a browser
- check VPN or lab routing
- verify the IP in `fmc_orchestrator.py` matches your FMC

### SSL certificate warnings
This tool disables certificate verification (common in labs).  
If your environment requires strict TLS verification:
- you would enable verification in `requests.get/post(...)` calls and install a trusted certificate chain.

### YAML output selected but tool says PyYAML missing
Install:

```bash
pip install pyyaml
```

### “items” key missing / endpoint behaves differently
Some FMC endpoints return a single JSON object rather than a paginated `items` list.  
The pagination helper is designed to return the full object if `"items"` is absent.

If a particular endpoint has a unique paging model, a task may need a custom handler.

### Files have odd names
Task output filenames are “slugified” (cleaned) so they are safe for Linux/Windows filenames.  
Special characters are removed.

---

## Safety notes

- This tool **does not store** your password anywhere.
- Avoid copying tokens into notes/screenshots.
- Output files may contain sensitive security policy data — treat `outputs/` as sensitive.

---

## Quick “cheat sheet”

Run tool:

```bash
cd fmc_tool
python3 main.py
```

Where outputs go:

```
fmc_tool/outputs/<timestamp__domain-...__uuid-...>/
```

YAML vs JSON:
- Choose YAML (default) for readability
- Choose JSON for tooling / API fidelity

---

## Support / maintenance notes (for operators)

If a task fails:
- check `run_log.yaml` in the run folder
- the log entry should show which task was running and what domain was selected
- re-run the tool and repeat the failing task
