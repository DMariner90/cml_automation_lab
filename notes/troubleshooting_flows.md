# 🛠️ Troubleshooting Flow Library  

---

## 🔹 Session 3 – Users & Sudo  
*(See: [Session 3 Notes](session_3.md))*  

[Cannot run sudo]
↓
groups <user>
↓
┌───────────────┐
│ In sudo group?│──No──> sudo usermod -aG sudo <user>
└───────┬───────┘
↓ Yes
Check /etc/sudoers → visudo

yaml
Copy code

---

## 🔹 Session 4 – File Ownership  
*(See: [Session 4 Notes](session_4.md))*  

[Permission denied]
↓
ls -l <file>
↓
┌───────────────┐
│ Wrong owner? │──Yes──> sudo chown user:group file
└───────┬───────┘
↓ No
│ Missing perms?│──Yes──> chmod u+x file
↓
Else: check SELinux/AppArmor

yaml
Copy code

---

## 🔹 Session 5 – Processes & Services  
*(See: [Session 5 Notes](session_5.md))*  

[Process unresponsive]
↓
ps aux | grep <name>
↓
kill <PID>
↓
If still running → kill -9 <PID>

Copy code
[Service won’t start]
↓
systemctl status <service>
↓
┌───────────────────┐
│ Active=failed ? │
└──────────┬────────┘
↓
journalctl -u <service>
↓
Config/dependency issue → fix & restart

yaml
Copy code

---

## 🔹 Notes
- Always start with `ls -l`, `ps aux`, or `systemctl status` for context.  
- Use `journalctl` to investigate service failures.  
- Always verify after applying a fix. 

---

## 🔹 Session 6 – File Permissions  
*(See: [Session 6 Notes](session_6.md))*  

[Permission denied]
↓
ls -l <file>
↓
┌───────────────┐
│ Owner correct?│──No──> sudo chown user file
└───────┬───────┘
↓ Yes
┌─────────────────────┐
│ Missing permissions?│──Yes──> chmod u+r file
└─────────┬───────────┘
↓ No
Check special bits (sticky, setuid, setgid)


[SSH fails]
    ↓
systemctl status ssh
    ↓
Enable: sudo systemctl enable --now ssh
    ↓
Check logs: journalctl -u ssh



### Session 7 – Linux Fundamentals Recap  

[Permission denied when accessing file]  
    ↓  
ls -l file  
    ↓  
Check owner/group → sudo chown user:group file  
    ↓  
Check permissions → sudo chmod 640 file  
    ↓  
✅ Expected Fix: User can now access/read file.  

[user is not in sudoers file]  
    ↓  
groups user  
    ↓  
sudo usermod -aG sudo user  
    ↓  
sudo visudo → confirm %sudo group enabled  
    ↓  
✅ Expected Fix: User can run sudo commands.  

[ssh: connect to host <IP> port 22: Connection refused]  
    ↓  
sudo systemctl status ssh  
    ↓  
sudo systemctl enable --now ssh  
    ↓  
journalctl -u ssh  
    ↓  
✅ Expected Fix: SSH is active and remote logins work.  

