# 📘 Linux Command Reference – Milestone 1 + Ubuntu CLI  

This file combines all commands practiced in Milestone 1 
Commands are grouped by category for quick reference. 

---

## 🔹 System Information
| Command | Description |
|---------|-------------|
| `uname -a` | Show system/kernel info |
| `hostnamectl` | Show hostname and related details |
| `lscpu` | CPU architecture info |
| `timedatectl status` | Show system time |

---

## 🔹 System Monitoring & Management
| Command | Description |
|---------|-------------|
| `top` | Real-time processes |
| `htop` | Interactive process viewer |
| `df -h` | Disk usage (human-readable) |
| `free -m` | Memory usage in MB |
| `ps aux` | Snapshot of all processes |
| `kill <PID>` | Terminate process |
| `kill -9 <PID>` | Force terminate |
| `jobs` | Show background jobs |
| `<cmd> &` | Run in background |
| `fg <job>` | Bring job to foreground |

---

## 🔹 Services & Logs
| Command | Description |
|---------|-------------|
| `sudo systemctl start/stop/status/restart <service>` | Manage services |
| `sudo systemctl enable/disable <service>` | Enable/disable at boot |
| `sudo systemctl reload <service>` | Reload service config |
| `journalctl -f` | Follow logs in real time |
| `journalctl -u <service>` | Logs for a service |

---

## 🔹 Scheduling
| Command | Description |
|---------|-------------|
| `crontab -e` | Edit cron jobs |
| `crontab -l` | List cron jobs |

---

## 🔹 File Management
| Command | Description |
|---------|-------------|
| `ls -l` | List files (long format) |
| `pwd` | Print working directory |
| `cd <dir>` | Change directory |
| `mkdir <dir>` | Create directory |
| `rm -r <dir>` | Remove directory recursively |
| `touch <file>` | Create/update empty file |
| `cp <src> <dst>` | Copy file |
| `mv <src> <dst>` | Move/rename file |
| `rm <file>` | Delete file |

---

## 🔹 File Viewing & Editing
| Command | Description |
|---------|-------------|
| `cat <file>` | Print contents |
| `less <file>` | Scroll through file |
| `nano <file>` | Edit file |
| `head <file>` | Show first lines |
| `tail <file>` | Show last lines |

---

## 🔹 Ownership & Permissions
| Command | Description |
|---------|-------------|
| `chmod [who][+/-][perm] <file>` | Change permissions |
| `chmod 644 file` | rw-r--r-- |
| `chmod 755 file` | rwxr-xr-x |
| `chmod u+x file` | Add execute for owner |
| `chmod g-w file` | Remove write for group |
| `chmod -R 755 dir` | Recursive chmod |
| `chmod 1777 dir` | Sticky bit |
| `chown user file` | Change owner |
| `chown user:group file` | Change owner+group |
| `chgrp group file` | Change group |

---

## 🔹 Searching & Finding
| Command | Description |
|---------|-------------|
| `find <dir> -name <pattern>` | Find files by name |
| `grep <pattern> <file>` | Search in file |

---

## 🔹 Archiving & Compression
| Command | Description |
|---------|-------------|
| `tar -czvf file.tar.gz files` | Create archive |
| `tar -xvf file.tar.gz` | Extract archive |

---

## 🔹 Users & Groups
| Command | Description |
|---------|-------------|
| `who` / `w` | Show logged-in users |
| `id <user>` | Show UID/GID info |
| `groups <user>` | Show group memberships |
| `sudo adduser <name>` | Create user |
| `sudo deluser <name>` | Delete user |
| `sudo passwd <name>` | Set/change password |
| `sudo passwd -l <name>` | Lock account |
| `sudo passwd -u <name>` | Unlock account |
| `su <user>` | Switch user |
| `sudo chage <name>` | Manage password expiry |
| `sudo addgroup <group>` | Create group |
| `sudo delgroup <group>` | Delete group |
| `usermod -aG <group> <user>` | Add user to group |
| `visudo` | Safely edit sudoers |
| `sudo -l` | List allowed sudo commands |

---

## �� Networking
| Command | Description |
|---------|-------------|
| `ip addr show` | Show interfaces & IPs |
| `ip -s link` | Show NIC stats |
| `ss -l` | Show listening sockets |
| `ping <host>` | Ping host |
| `cat /etc/netplan/*.yaml` | View Netplan config |
| `sudo netplan try` | Test config |
| `sudo netplan apply` | Apply config |

---

## 🔹 Firewall (UFW)
| Command | Description |
|---------|-------------|
| `sudo ufw status` | Firewall status |
| `sudo ufw enable/disable` | Enable/disable firewall |
| `sudo ufw allow <port/service>` | Allow traffic |
| `sudo ufw deny <port/service>` | Deny traffic |
| `sudo ufw delete allow/deny <port/service>` | Delete rule |

---

## 🔹 SSH & Remote Access
| Command | Description |
|---------|-------------|
| `ssh user@host` | SSH login |
| `scp src user@host:dst` | Copy over SSH |
| `ssh-copy-id user@host` | Copy SSH key |

---

## 🔹 Package Management (APT)
| Command | Description |
|---------|-------------|
| `sudo apt update` | Update package lists |
| `sudo apt upgrade` | Upgrade packages |
| `sudo apt install <pkg>` | Install package |
| `sudo apt install -f --reinstall <pkg>` | Fix/reinstall |
| `apt search <pkg>` | Search package |
| `apt-cache policy <pkg>` | Show versions |
| `sudo apt remove <pkg>` | Remove package |
| `sudo apt purge <pkg>` | Remove package + config |

---

## 🔹 Package Management (Snap)
| Command | Description |
|---------|-------------|
| `snap find <pkg>` | Search snaps |
| `sudo snap install <pkg>` | Install snap |
| `sudo snap remove <pkg>` | Remove snap |
| `sudo snap refresh` | Update snaps |
| `snap list` | List snaps |
| `snap info <pkg>` | Snap info |

---

## 🔹 LXD (Containers & VMs)
| Command | Description |
|---------|-------------|
| `lxd init` | Initialize LXD |
| `lxc launch ubuntu:22.04 <name>` | Launch container |
| `lxc launch ubuntu:22.04 <name> --vm` | Launch VM |
| `lxc list` | List instances |
| `lxc start/stop <instance>` | Manage instance |
| `lxc delete <instance>` | Delete instance |
| `lxc exec <instance> -- bash` | Shell into instance |
| `lxc file pull/push` | Transfer files |
| `lxc project create <proj>` | Create project |
| `lxc project switch <proj>` | Switch project |

---

## 🔹 Ubuntu Pro
| Command | Description |
|---------|-------------|
| `sudo pro attach <token>` | Attach machine to Ubuntu Pro |
| `sudo pro status` | Show Pro service status |
| `sudo pro enable/disable <service>` | Enable/disable Pro service |
| `sudo pro refresh` | Refresh Pro state |
| `sudo pro detach` | Detach from Ubuntu Pro |

---
