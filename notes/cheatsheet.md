# 📘 Master Cheat Sheet – Linux Fundamentals  

---

## 🔹 Session 1 – Basic Commands
*(See: [Session 1 Notes](session_1.md))*
| Command | Description |
|---------|-------------|
| `ls -l` | List files in long format |
| `pwd` | Show current directory |
| `cd <dir>` | Change directory |
| `mkdir <dir>` | Create directory |
| `rm -r <dir>` | Remove directory recursively |

---

## 🔹 Session 2 – File Viewing & Editing
*(See: [Session 2 Notes](session_2.md))*
| Command | Description |
|---------|-------------|
| `cat file` | Print file contents |
| `less file` | View file with scrolling |
| `nano file` | Edit file |
| `cp file1 file2` | Copy file |
| `mv file1 file2` | Move/rename file |

---

## 🔹 Session 3 – Users, Groups & Sudo
*(See: [Session 3 Notes](session_3.md))*
| Command | Description |
|---------|-------------|
| `adduser <name>` | Create new user |
| `passwd <name>` | Set/change password |
| `usermod -aG <group> <user>` | Add user to group |
| `deluser <name>` | Delete user |
| `delgroup <name>` | Delete group |
| `visudo` | Safely edit sudoers |
| `sudo -l` | List allowed sudo commands |

---

## 🔹 Session 4 – File Ownership
*(See: [Session 4 Notes](session_4.md))*
| Command | Description |
|---------|-------------|
| `chown user file` | Change owner |
| `chown user:group file` | Change owner + group |
| `chgrp group file` | Change group only |
| `-R` | Recursive for dirs |

---

## 🔹 Session 5 – Processes & Services
*(See: [Session 5 Notes](session_5.md))*
| Command | Description |
|---------|-------------|
| `ps aux` | Snapshot of all processes |
| `top` | Interactive process monitor |
| `htop` | Enhanced top |
| `kill <PID>` | Terminate process |
| `kill -9 <PID>` | Force terminate |
| `systemctl start/stop/status/restart <service>` | Manage services |
| `systemctl enable/disable <service>` | Boot-time control |
| `journalctl -u <service>` | View service logs |

---

## 🔹 Session 6 – File Permissions (chmod Deep Dive)
*(See: [Session 6 Notes](session_6.md))*
| Command | Description |
|---------|-------------|
| `chmod 644 file` | rw-r--r-- |
| `chmod 755 file` | rwxr-xr-x |
| `chmod u+x file` | add execute for owner |
| `chmod g-w file` | remove write for group |
| `chmod -R 755 dir` | recursive chmod |
| `chmod 1777 dir` | sticky bit example |


## 🔹 Session 7 – Linux Fundamentals Recap  
*(See: [Session_7 Notes](session_7.md))*  

| Command | Description | Expected Result |  
|---------|-------------|-----------------|  
| `systemctl enable --now ssh` | Start and enable SSH at boot | `active (running)` in `systemctl status ssh` |  
| `chmod 1777 dir` | Set sticky bit on directory | `drwxrwxrwt` in `ls -ld` output |  
| `echo -e '#!/bin/bash\necho "Automation Ready"' | sudo tee run.sh` | Quick script creation | Script prints `Automation Ready` |  


## 🔹 Session 9 – Python Virtual Environments & Package Management  
*(See: [Session_9 Notes](session_9.md))*  

| Command | Description | Expected Result |  
|---------|-------------|-----------------|  
| `python3 -m venv .venv` | Create venv | `.venv/` created |  
| `source .venv/bin/activate` | Activate venv | `(.venv)` prompt |  
| `pip install <pkg>` | Install library | Installed in venv |  
| `pip list` | List libraries | Shows installed pkgs |  
| `pip freeze > requirements.txt` | Save versions | File populated |  
| `deactivate` | Exit venv | Prompt returns normal |  


## 🔹 Session 10 – Python Basics: Variables, Data Types & Input/Output  
*(See: [Session_10 Notes](session_10.md))*  

| Command / Syntax | Description | Expected Result |  
|------------------|-------------|-----------------|  
| `device_name = "Router1"` | String variable | Stores text |  
| `port = 22` | Integer variable | Stores number |  
| `is_active = True` | Boolean variable | True/False value |  
| `devices = ["R1","R2"]` | List | Ordered collection |  
| `credentials = {"user":"admin"}` | Dictionary | Key/value pairs |  
| `print(f"Device: {device_name}")` | f-string output | Prints variable inline |  
| `input("Enter name: ")` | Get user input | Returns string from user |  
| `int(input("Enter port: "))` | Input conversion | Returns integer |  
