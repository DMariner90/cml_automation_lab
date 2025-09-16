📘 Session 1 – WSL2 Setup & First Linux Commands

File: notes/session_1.md

---
session: 1
date: 2025-09-16
milestone: 0 – Dev Environment Setup
topic: WSL2 Setup & First Linux Commands
duration: 2h
tags: [linux, basics, navigation, exam]
related: []
ENAUTO_obj: 1.1
---

# 📘 Session 1 – WSL2 Setup & First Linux Commands  

---

## 📖 Introduction
Linux navigation and basic file management form the foundation for all system administration. Without these commands, you cannot move around the filesystem, organize data, or script automated workflows.  
This is directly relevant to automation: tools like Python and Ansible rely on predictable directory structures and permissions to function correctly.  

---

## 🧪 Lesson Steps (Guided Labs)
```bash
pwd                  # print working directory (where you are now)
ls                   # list files in current directory
ls -l                # long format: perms, owner, size, date
cd /path             # change directory
mkdir test           # create a new directory
rm -r test           # remove directory recursively

🔎 Review / Recap

Practiced moving around the filesystem with cd.

Listed files with ls, including metadata with ls -l.

Created and removed directories with mkdir and rm -r.

Automation tie-in: scripts and playbooks must reference paths accurately.

ENAUTO Objective: 1.1 – Linux Fundamentals.

⚡ Troubleshooting
[Command fails: No such file or directory]
        ↓
   Check path with pwd
        ↓
   If wrong → cd to correct dir

[Permission denied]
        ↓
   Are you in your home dir?
        ↓
 If not → need sudo

🧪 Challenge Lab
Setup
mkdir -p labs/session1_demo
cd labs/session1_demo

Scenario

You need to organize some files into folders for automation.

Tasks

Create 3 empty files (touch file1.txt file2.txt file3.txt).

Make a new directory archive/.

Move all 3 files into archive/.

Delete archive/ and its contents.

📑 Cheat Sheet
Command	Description
pwd	Show current dir
ls -l	Detailed listing
cd	Change directory
mkdir	Create directory
rm -r	Remove directory recursively
🧠 Self-Check

What does pwd display?

Difference between ls and ls -l?

How to create nested directories in one command?

✅ Answers

The absolute path of the current working directory.

ls shows file names only; ls -l adds permissions, owner, group, size, and timestamps.

mkdir -p parent/child.

🔍 Command Lens: ls

Purpose: List directory contents.

Anatomy: ls [OPTIONS] [PATH]

Common flags: -l (long), -a (all, including hidden), -h (human-readable sizes).

Failures: “No such file or directory” → wrong path.

📚 Glossary

Directory: A folder in the filesystem.

Path: The location of a file/directory in the hierarchy.

Working directory: The folder your shell is currently in
