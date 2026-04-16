# FMC Tool — How to Add a New Task

This guide explains how to add new “tasks” to **fmc_tool** so others can extend it safely.

---

## What is a “task”?

A **task** is a single unit of work the tool can perform against FMC.

Examples:
- Get access rules for selected policies
- Get all network objects
- Get interfaces for selected devices
- Get NAT policies

Tasks live in the `tasks/` folder, and each task is a Python file that exposes:

```python
def run(access_token: str, ctx: RunContext) -> None:
    ...
```

Where:
- `access_token` is the FMC API token (already authenticated)
- `ctx` is the shared run context:
  - domain name / uuid
  - run folder path
  - output format (yaml/json)
  - FMC host

---

## What you need to change to add a task

Adding a new task requires **3 steps**:

1) Create the task file in `tasks/`
2) Import it in `main.py`
3) Add it to the task menu + dispatch logic in `main.py`

That’s it.

---

## Step-by-step instructions

### Step 1 — Create a new task file

Create a new file in:

```
fmc_tool/tasks/
```

Name it with a clear “verb + object” style, for example:

- `get_intrusion_policies.py`
- `get_audit_logs.py`
- `get_deployment_queue.py`
- `get_tasks_status.py`

---

### Step 2 — Use the task template

Copy this template and edit only the parts you need.

> **Tip:** Keep the task name in the log and output filenames consistent with the filename.

#### Generic Task Template (GET + write output)

```python
\"\"\"
TASK: <Describe what this task does in one sentence>

Inputs:
- access_token: FMC API access token
- ctx: RunContext (domain info, run folder, output format)

Behavior:
- calls one or more FMC endpoints
- writes output(s) into the per-run folder
- appends a task entry to the run log
\"\"\"

from fmc_orchestrator import (
    BASE_URL,
    RunContext,
    append_run_log,
    fmc_get_all_items,
    write_output,
)


def run(access_token: str, ctx: RunContext) -> None:
    task_name = "<your_task_name_here>"  # e.g. "get_intrusion_policies"

    # Always log that the task started (helpful for troubleshooting)
    append_run_log(
        ctx,
        {
            "task": task_name,
            "event": "started",
            "output_format": ctx.output_format,
        },
    )

    # ----- UPDATE THIS URL -----
    url = f\"{BASE_URL}/api/fmc_config/v1/domain/{ctx.domain_uuid}/<your/endpoint/here>\"

    # GET data (pagination helper handles offset/limit if supported)
    data = fmc_get_all_items(access_token, url)

    # Write output
    out_path = write_output(ctx, file_stem=task_name, payload=data)

    append_run_log(
        ctx,
        {
            "task": task_name,
            "event": "finished",
            "saved_to": str(out_path),
        },
    )

    print(f\"Saved output -> {out_path}\")
```

---

### Step 3 — Register the task in `main.py`

#### (A) Import the new task

At the top of `main.py` where tasks are imported, add your new task:

```python
from tasks import (
    get_rules,
    get_network_objects,
    get_interfaces,
    get_nat_policies,
    get_intrusion_policies,   # <-- NEW
)
```

#### (B) Add it to the task menu

Update the `choose_task()` menu:

```python
print("5) Get all intrusion policies for this domain")
```

Make sure the numbering matches what you’ll check in the dispatcher.

#### (C) Dispatch it

In the task dispatch section of `main.py`, add:

```python
elif task_choice == "5":
    append_run_log(ctx, {"task": "get_intrusion_policies", "output_format": ctx.output_format})
    get_intrusion_policies.run(access_token, ctx)
```

---

## Common patterns for task development

### 1) If the task needs a policy selection
Use orchestrator helpers:

- `fmc_list_policies(access_token, ctx.domain_uuid)`
- `select_policies(policies)`

Example:

```python
from fmc_orchestrator import fmc_list_policies, select_policies

policies = fmc_list_policies(access_token, ctx.domain_uuid)
selected, note = select_policies(policies)
append_run_log(ctx, {"task": "my_task", "policy_selection": note})
```

Then loop `selected`.

### 2) If the task needs a device selection
Use orchestrator helpers:

- `fmc_list_devices(access_token, ctx.domain_uuid)`
- `select_devices(devices)`

### 3) If the task writes multiple output files
Use a consistent naming convention:

- `taskname__policy-<name>`
- `taskname__device-<name>`
- `taskname__object-<id>`

Example:

```python
write_output(ctx, f"my_task__policy-{policy_name}", payload)
```

---

## How to choose a good task name

Good task names are:
- explicit and readable
- start with a verb (“get”, “export”, “list”, “clone”, “update”)
- match what the task actually does

Examples:
- `get_audit_logs`
- `get_deployment_queue`
- `export_access_policies`
- `clone_access_policy`
- `bulk_update_rules`

---

## Troubleshooting task development

### Task runs when importing (bad)
If a task has code **outside** the `run()` function, it may execute at import time.

✅ Correct:
- only define functions at module level
- all work happens inside `run()`

❌ Incorrect:
```python
append_run_log(ctx, {...})  # ctx doesn't exist at import time
```

### Pagination surprises
Some FMC endpoints return:
- a paginated `{"items": [...]}` structure
- OR a single object without `items`

The helper `fmc_get_all_items()` returns:
- a flat list for `items` endpoints
- the full JSON object for non-`items` endpoints

If an endpoint has a different paging model, implement a custom paging loop in the task.

### Output format errors
If YAML is selected and PyYAML isn’t installed:

```bash
pip install pyyaml
```

---

## Optional improvement: A “task registry”
Right now tasks are registered manually in `main.py`.

If you add many tasks, you might later want:
- a registry dict mapping menu numbers to task modules
- automatic menu generation

This is optional and not required for the current tool.

---

## Quick example: Add “Get Intrusion Policies”

1) Create: `tasks/get_intrusion_policies.py` using the template.
2) Import in `main.py`
3) Add menu entry “5) Get all intrusion policies…”
4) Add dispatcher `elif task_choice == "5": ...`

Done.

---

## Checklist (copy/paste)

- [ ] Create file `tasks/<new_task>.py`
- [ ] Ensure it exposes `run(access_token, ctx)`
- [ ] Use `append_run_log` at start and end
- [ ] Use `fmc_get_all_items` for collection endpoints
- [ ] Use `write_output` to save artifacts
- [ ] Import task in `main.py`
- [ ] Add a menu option in `choose_task()`
- [ ] Add dispatch logic in `main.py`
