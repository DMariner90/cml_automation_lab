
---

# 📘 Session 5 – Processes & Services  
File: `notes/session_5.md`  

```markdown
---
session: 5
date: 2025-09-19
milestone: 1 – Linux & Server Fundamentals
topic: Processes & Services
duration: 2h
tags: [linux, processes, services, systemctl, exam]
related: [Session 4 – File Ownership & Groups]
ENAUTO_obj: 1.1
---

# 📘 Session 5 – Processes & Services  

---

## 📖 Introduction
Every action on a Linux system is a process. Services are special background processes managed by systemd.  
Understanding process management is critical for diagnosing resource issues and ensuring automation systems start required services correctly.  

---

## 🧪 Lesson Steps (Guided Labs)
```bash
ps aux | head -5                         # list processes
top                                      # live monitor
sudo apt install -y htop && htop         # nicer interactive monitor

sleep 500 &                              # start process
ps aux | grep sleep
kill <PID>                               # terminate process
kill -9 <PID>                            # force kill
ps aux | grep sleep                      # confirm

sudo apt install -y openssh-server       # install ssh service
systemctl status ssh                     # check service status
sudo systemctl stop ssh                  # stop
sudo systemctl start ssh                 # start
sudo systemctl restart ssh               # restart
sudo systemctl disable ssh               # disable at boot
sudo systemctl enable ssh                # enable at boot

systemctl list-units --type=service | head -10
systemctl list-unit-files --type=service | grep enabled | head -10
journalctl -u ssh --no-pager | tail -10
🔎 Review / Recap
Viewed and killed processes.

Monitored interactively with top and htop.

Installed OpenSSH server and managed its lifecycle.

Verified logs with journalctl.

Automation tie-in: Automation often requires services to be running (SSH, web servers).

ENAUTO Objective: 1.1 – Linux Fundamentals.

⚡ Troubleshooting
perl
Copy code
[Process unresponsive]
        ↓
 ps aux | grep <name>
        ↓
 kill <PID>
        ↓
 If still alive → kill -9
csharp
Copy code
[Service not found]
        ↓
Package not installed
        ↓
Fix: sudo apt install <package>
php-template
Copy code
[Service won’t start]
        ↓
 systemctl status <service>
        ↓
 journalctl -u <service>
🧪 Challenge Lab
Setup
bash
Copy code
# create cpu hog
yes > /dev/null &
Scenario
System is slow; a process hogs CPU.

Tasks
Identify culprit with top/htop.

Kill process gracefully.

If needed, force kill.

Verify it’s gone.

Check logs for ssh service.

📑 Cheat Sheet
Command	Description
ps aux	List processes
top/htop	Monitor
kill <PID>	Terminate
systemctl start/stop/status	Manage services
systemctl enable/disable	Boot control
journalctl -u	Logs

🧠 Self-Check
What do a, u, x mean in ps aux?

Default signal for kill?

Difference: systemctl stop vs disable?

How to view logs for cron?

When to use kill -9?

✅ Answers
a all users, u user, x no terminal.

SIGTERM.

Stop = now, disable = boot.

journalctl -u cron.

When normal SIGTERM fails.

🔍 Command Lens: systemctl
Purpose: Manage systemd services.

Actions: start, stop, restart, status, enable, disable.

Failures: Service missing → install package.

📚 Glossary
PID: Process ID.

Daemon: Background service.

systemd: Init system + service manager.
