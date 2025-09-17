
---

### 2️⃣ `notes/cheatsheet.md` Update

```markdown
## 🔹 Session 8 – Intel NUC Ubuntu Server Setup  
*(See: [Session_8 Notes](session_8.md))*  

| Command | Description | Expected Result |  
|---------|-------------|-----------------|  
| `sudo nano /etc/netplan/01-netcfg.yaml` | Edit Netplan config | File opens for edit |  
| `sudo netplan apply` | Apply network config | Static IP live |  
| `ssh-copy-id user@IP` | Copy SSH key to user | Key added to authorized_keys |  
| `sudo nano /etc/ssh/sshd_config` | Edit SSH daemon config | Disable password logins |  
| `sudo systemctl restart ssh` | Restart SSH service | Config applied |  
| `sudo ufw allow OpenSSH` | Allow SSH traffic | SSH open in firewall |  
| `sudo ufw enable` | Enable firewall | Firewall active |  
