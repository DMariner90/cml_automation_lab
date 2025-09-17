# 📘 Milestone 1 Summary – Linux & Server Fundamentals  

**Sessions Covered:** 1–8  
**Focus:** Building core Linux server administration skills to support automation and Cisco Modeling Labs (CML).  

---

## ✅ Key Outcomes
- Installed and configured **Ubuntu (WSL2 + Intel NUC bare metal)**.  
- Learned **basic Linux commands** for navigation, file handling, and editing.  
- Managed **users, groups, and sudo privileges** securely.  
- Practiced **ownership, permissions, and sticky bit** for multi-user environments.  
- Monitored **processes and services** using `ps`, `kill`, `systemctl`, and `journalctl`.  
- Configured a **static IP** with Netplan and hardened SSH to **key-only authentication**.  
- Enabled **UFW firewall** and created a dedicated **service account (cmladmin)**.  

---

## 🔑 Commands Mastered
- **Navigation & Files:** `ls`, `pwd`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `nano`, `cat`, `less`  
- **Users & Groups:** `adduser`, `passwd`, `usermod`, `groups`, `deluser`, `delgroup`, `visudo`  
- **Ownership & Permissions:** `chown`, `chgrp`, `chmod`, `ls -l`, sticky bit (`chmod 1777`)  
- **Processes & Services:** `ps aux`, `top`, `kill`, `systemctl`, `journalctl`  
- **Networking & SSH:** `ip addr`, `ip link`, `ping`, `ssh`, `ssh-copy-id`, `netplan apply`  
- **Security:** `ufw allow OpenSSH`, `ufw enable`  

---

## 🧪 Challenge Labs Completed
1. **Sticky Bit Lab:** Shared directory where only file owners can delete their files.  
2. **Process Management:** Started & killed processes (`sleep`, `kill`).  
3. **SSH Hardening:** Key-only authentication, disabled passwords.  
4. **Static IP Setup:** Configured persistent networking with Netplan.  
5. **Service Account Isolation:** `cmladmin` user for lab operations.  

---

## 🚀 Why This Matters
Linux is the foundation of network automation. By mastering file permissions, user management, processes, and networking, you now have the **confidence to administer a server securely**. These skills will carry forward into:  
- Running **CML on bare metal**.  
- Deploying **automation tools** like Python, Ansible, and Docker.  
- Preparing for **exam scenarios** that require troubleshooting Linux environments.  

---

## 📚 Next Milestone – Python for Network Automation
- Python environment setup & package management.  
- Core scripting (variables, loops, functions).  
- Working with JSON/YAML data.  
- APIs and automation fundamentals.  
- Capstone mini-project before moving to CML.  
