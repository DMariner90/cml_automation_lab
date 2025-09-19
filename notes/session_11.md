# 📘 Session 11 – Sep 25, 2025  
**Topic:** Python Basics – Control Flow (if/else, loops) + Code Formatting & Linting  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- `if/else` statements let Python make decisions.  
- `for` loops iterate over lists (e.g., devices in an inventory).  
- `while` loops repeat until a condition is false (e.g., retries).  
- `break` and `continue` control loop behavior.  
- **Black** formats Python code for consistency.  
- **Ruff** lints code to catch errors and style issues.  
- Adding Black + Ruff to post-flight keeps the repo clean and professional.  

---

## 💻 Commands & Examples  

```python
# If/else
device_reachable = True
if device_reachable:
    print("Device is reachable")
else:
    print("Device is not reachable")

# For loop
devices = ["R1", "R2", "R3"]
for d in devices:
    print(f"Connecting to {d}...")

# While loop
count = 1
while count <= 3:
    print(f"Attempt {count}")
    count += 1
✅ Expected Output:

vbnet
Copy code
Device is reachable
Connecting to R1...
Connecting to R2...
Connecting to R3...
Attempt 1
Attempt 2
Attempt 3
🔎 Review / Recap
if/else controls logic flow.

for loops = device iteration.

while loops = retry/polling.

break exits loops, continue skips to next iteration.

Black auto-formats; Ruff enforces clean code.

⚡ Troubleshooting
Black fails “Cannot parse” → check for invalid Python, remove stray lines, rerun.

Ruff error “unrecognized subcommand” → must use ruff check file.py.

Wrong logic/output → print debug values, confirm conditions.

While loop never ends → ensure loop variable increments.

🧪 Challenge Lab
Write labs/loop_devices.py to:

Store list: ["R1","SW1","FW1"].

Ping each device (print).

Use if to decide reachability (reachable if startswith "R").

Retry up to 3 attempts with a while loop.

�� Challenge Lab Walkthrough
python
Copy code
devices = ["R1", "SW1", "FW1"]
MAX_ATTEMPTS = 3

for d in devices:
    print(f"\n=== Checking {d} ===")
    attempt = 1
    success = False

    while attempt <= MAX_ATTEMPTS:
        print(f"Attempt {attempt}: Pinging {d}...")
        if d.startswith("R"):
            print(f"✅ Device {d} reachable (on attempt {attempt})")
            success = True
            break
        attempt += 1

    if not success:
        print(f"❌ Device {d} unreachable after {MAX_ATTEMPTS} attempts")
✅ Expected Output:

yaml
Copy code
=== Checking R1 ===
Attempt 1: Pinging R1...
✅ Device R1 reachable (on attempt 1)

=== Checking SW1 ===
Attempt 1: Pinging SW1...
Attempt 2: Pinging SW1...
Attempt 3: Pinging SW1...
❌ Device SW1 unreachable after 3 attempts

=== Checking FW1 ===
Attempt 1: Pinging FW1...
Attempt 2: Pinging FW1...
Attempt 3: Pinging FW1...
❌ Device FW1 unreachable after 3 attempts
🧠 Self-Check + ✅ Answers
for vs while → for iterates known lists, while repeats until condition false.

break exits loop early.

continue skips to next iteration.

Black vs Ruff → Black formats, Ruff lints.

Code example → prints Router found: R1, Not a router: SW1.

📚 Glossary
Term	Definition	Why it matters
if/else	Conditional branching	Decision making in scripts
for loop	Iterates over items	Apply tasks across devices
while loop	Runs until false	Retry/polling automation
break	Exits loop	Stop early on success
continue	Skip iteration	Skip failed devices
Black	Auto-formatter	Consistent clean code
Ruff	Linter	Catch mistakes fast
