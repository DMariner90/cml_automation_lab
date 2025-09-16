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

