# 📘 Session 14 – File I/O (Configs & Logs)  
**Date:** Sep 23, 2025  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- How to **read files** with `.read()` (whole file) and `.readlines()` (list of lines).  
- How to **write logs** with `"w"` (overwrite) and `"a"` (append).  
- Why **context managers** (`with open(...)`) are best practice → auto-close files.  
- How to combine file I/O with automation use cases: configs, inventories, logs.  

---

## 💻 Code & Concepts Practiced  

### Reading configs  
```python
with open("labs/router.cfg", "r") as f:
    config = f.read()   # entire file
Writing logs
python
Copy code
with open("labs/connection_log.txt", "w") as f:
    f.write("Connecting to R1... SUCCESS\n")
Appending logs
python
Copy code
with open("labs/connection_log.txt", "a") as f:
    f.write("Connecting to SW1... SUCCESS\n")
Context manager best practice
python
Copy code
with open("labs/connection_log.txt", "a") as f:
    for dev in ["R1", "R2"]:
        f.write(f"Device {dev} processed.\n")
🔎 Review / Recap
Read → Write → Append is the standard file I/O workflow.

Context managers (with) should always be used in production scripts.

Logs are critical for automation, configs are common inputs/outputs.

Appending ensures historical data isn’t lost.

⚡ Troubleshooting
FileNotFoundError → Wrong path or file doesn’t exist. Fix: ls labs/ to verify.

PermissionError → Trying to write where user has no rights. Fix: check ownership.

Truncated log → Used "w" instead of "a". Fix: change mode.

🧪 Challenge Lab
Task: Read devices from devices.txt, log simulated connections.

✅ Expected Result:

csharp
Copy code
Devices loaded from file: ['R1', 'R2', 'SW1', 'FW1']
Connecting to R1... SUCCESS
...
🏋️ Stretch Challenge
Task: Parse router config, extract interface lines into interfaces.txt.

✅ Expected Result:

kotlin
Copy code
interface Gig0/0
interface Gig0/1
🧠 Self-Check + ✅ Answers
What’s the difference between "w" and "a"?
→ "w" overwrites, "a" appends.

How do you safely ensure files are closed?
→ Use with open(...) as f:.

What’s the output type of .readlines()?
→ List of strings, one per line.

Why are logs important in automation?
→ They provide traceability and troubleshooting.

📚 Glossary
File handle → The reference returned by open().

Context manager → Python structure that manages resources (with).

Overwrite vs append → "w" replaces file, "a" preserves existing data.

💭 Last Thoughts
File I/O is where Python touches the real world: configs, logs, inventories.
It’s also the bridge to working with APIs and structured data (JSON/YAML) in upcoming sessions.
