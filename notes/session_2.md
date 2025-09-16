📘 Session 2 – File Viewing & Editing

File: notes/session_2.md

---
session: 2
date: 2025-09-17
milestone: 1 – Linux & Server Fundamentals
topic: File Viewing & Editing
duration: 2h
tags: [linux, files, editing, exam]
related: [Session 1 – Basic Commands]
ENAUTO_obj: 1.1
---

# 📘 Session 2 – File Viewing & Editing  

---

## 📖 Introduction
Being able to view and edit files is essential for working with Linux systems.  
System configs, logs, and scripts all live in text files — if you can’t read and modify them confidently, automation and troubleshooting grind to a halt.  

---

## 🧪 Lesson Steps (Guided Labs)
```bash
cat /etc/os-release         # view OS release info
less /etc/passwd            # scroll through system users
nano test.txt               # edit or create a file in nano
cp test.txt copy.txt        # copy a file
mv copy.txt moved.txt       # rename or move a file
rm moved.txt                # delete a file

🔎 Review / Recap

Learned to use cat and less to view files.

Practiced editing with nano.

Managed files using cp, mv, and rm.

Automation tie-in: Python and Ansible configs are just text files. Knowing how to inspect/edit is critical.

ENAUTO Objective: 1.1 – Linux Fundamentals.

⚡ Troubleshooting
[rm fails: No such file]
        ↓
Check filename with ls
        ↓
Typo? → correct and retry

[Permission denied editing file]
        ↓
Is file owned by root?
        ↓
If yes → sudo nano <file>

🧪 Challenge Lab
Setup
mkdir -p labs/session2_demo
cd labs/session2_demo

Scenario

You’re asked to prepare a simple config file.

Tasks

Create a file config.txt with 3 lines of text.

Copy it to backup_config.txt.

Rename backup_config.txt to config.old.

Delete config.old.

📑 Cheat Sheet
Command	Description
cat	Print file contents
less	Scroll view a file
nano	Edit/create a file
cp	Copy files
mv	Move/rename files
rm	Delete files
🧠 Self-Check

When to use cat vs less?

How do you rename a file?

How do you delete a file as root?

✅ Answers

Use cat for short files; less for longer, scrollable files.

mv old new.

sudo rm file.

🔍 Command Lens: nano

Purpose: Text editor.

Keys: Ctrl+O save, Ctrl+X exit.

Failures: “Permission denied” → need sudo.

📚 Glossary

stdout: Standard output, where cat prints.

editor: Tool for modifying text files.
