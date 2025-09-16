
---

# 📘 Session 4 – File Ownership & Groups  
File: `notes/session_4.md`  

```markdown
---
session: 4
date: 2025-09-18
milestone: 1 – Linux & Server Fundamentals
topic: File Ownership & Groups
duration: 2h
tags: [linux, ownership, permissions, exam]
related: [Session 3 – Users, Groups & Sudo]
ENAUTO_obj: 1.1
---

# 📘 Session 4 – File Ownership & Groups  

---

## 📖 Introduction
Ownership defines who controls a file and which group has shared access. Misaligned ownership is a top cause of permission errors.  
Automation systems regularly copy configs and must set ownership correctly, or scripts fail silently.  

---

## 🧪 Lesson Steps (Guided Labs)
```bash
mkdir -p labs/ownership_demo && cd labs/ownership_demo
echo "demo" > demo.txt
ls -l

sudo chown david:david demo.txt
ls -l demo.txt

sudo chgrp -R users labs/ownership_demo
ls -l

sudo chown -R david:users labs/ownership_demo
ls -l

find labs/ownership_demo -maxdepth 2 -printf "%u %g %p\n"
rm -rf labs/ownership_demo
🔎 Review / Recap
Practiced changing ownership with chown and chgrp.

Used recursion for whole directories.

Verified with ls -l and find.

Automation tie-in: File ownership errors break automation runs.

ENAUTO Objective: 1.1 – Linux Fundamentals.

⚡ Troubleshooting
sql
Copy code
[invalid group]
        ↓
Check /etc/group
csharp
Copy code
[Operation not permitted]
        ↓
File owned by root
        ↓
Fix with sudo
sql
Copy code
[Only one file changed]
        ↓
Forgot -R
🧪 Challenge Lab
Setup
bash
Copy code
mkdir -p labs/app
sudo touch labs/app/config.yaml
Scenario
A tarball was extracted as root; user can’t edit files.

Tasks
Verify ownership with ls -l.

Recursively change to david:users.

Verify with find.

📑 Cheat Sheet
Command	Description
chown user file	Change owner
chown user:group	Change owner & group
chgrp group	Change group only
-R	Recursive

🧠 Self-Check
What does chown user:group file do?

What is the difference between chown and chgrp?

What flag applies recursively?

✅ Answers
Sets both owner and group.

chown changes owner; chgrp only changes group.

-R.

🔍 Command Lens: chown
Purpose: Change ownership.

Anatomy: chown [OPTIONS] user:group path.

Flags: -R recursive.

Failure: Wrong group → check with /etc/group.

📚 Glossary
Owner: User with primary control.

Group: Shared permissions role.


