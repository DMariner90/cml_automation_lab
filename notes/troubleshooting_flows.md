# 🛠️ Troubleshooting Flow Library  

---

## 🔹 Session 3 – Users & Sudo
[Cannot run sudo]
↓
groups <user>
↓
┌───────────────┐
│ In sudo group?│──No──> usermod -aG sudo <user>
└───────┬───────┘
↓ Yes
Check /etc/sudoers → visudo


---

## 🔹 Session 4 – File Ownership


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


---

## 🔹 Session 5 – Processes & Services


[Process unresponsive]
↓
ps aux | grep <name>
↓
kill <PID>
↓
If still running → kill -9 <PID>

[Service won’t start]
↓
systemctl status <service>
↓
Active=failed?
↓
journalctl -u <service>
↓
Config/dependency issue → fix & restart

