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


### Session 8 – Intel NUC Ubuntu Server Setup  

[Static IP not applying]  
    ↓  
Check NIC name → ip link  
    ↓  
Validate YAML syntax → sudo netplan try  
    ↓  
Apply config → sudo netplan apply  
    ↓  
✅ Fix: IP visible via ip addr  

[SSH still asking for password]  
    ↓  
Check authorized_keys exists → ls -la ~/.ssh  
    ↓  
Re-copy key → ssh-copy-id user@IP  
    ↓  
Verify sshd_config → PubkeyAuthentication yes, PasswordAuthentication no  
    ↓  
Restart SSH → sudo systemctl restart ssh  
    ↓  
✅ Fix: Key-only login works  

[UFW blocking connection]  
    ↓  
Check rules → sudo ufw status  
    ↓  
Add SSH rule → sudo ufw allow OpenSSH  
    ↓  
✅ Fix: SSH access restored  


### Session 9 – Python Virtual Environments & Package Management  

[pip not found]  
    ↓  
sudo apt install python3-pip -y  
    ↓  
✅ Fix: pip available  

[.venv not activating]  
    ↓  
Check → source .venv/bin/activate  
    ↓  
✅ Fix: venv active  

[ImportError running script]  
    ↓  
pip install <missing-package>  
    ↓  
✅ Fix: script runs successfully  

### Session 10 – Python Basics: Variables, Data Types & Input/Output  

[Script won’t run with `python`]  
    ↓  
Check if venv is active → `which python`  
    ↓  
If points to `/usr/bin/python3`, reactivate venv:  
`source .venv/bin/activate`  
    ↓  
✅ Expected Fix: `python` now points to `.venv/bin/python`.  

---

[NameError: name 'variable' is not defined]  
    ↓  
Check for typos (Python is case-sensitive).  
    ↓  
✅ Expected Fix: Variable prints correctly after correction.  

---

[SyntaxError: invalid syntax]  
    ↓  
Check for missing `:` in dicts or mismatched quotes.  
    ↓  
✅ Expected Fix: Script runs without syntax errors.  

---

[`input()` always returns a string]  
    ↓  
Use `int(input(...))` for numeric input.  
    ↓  
✅ Expected Fix: Input stored as integer.  


### Session 11 – Python Basics: Control Flow + Linting  

[Black fails: "Cannot parse" error]  
    ↓  
Open file → check for invalid Python (e.g. pasted shell commands)  
    ↓  
Remove non-Python lines, save  
    ↓  
Re-run: black file.py  
    ↓  
✅ Expected Fix: Black reformats file successfully  

---

[Ruff error: "unrecognized subcommand"]  
    ↓  
Check command → must be `ruff check file.py` not just `ruff file.py`  
    ↓  
Re-run: ruff check file.py  
    ↓  
✅ Expected Fix: Ruff runs and reports issues  

---

[Script runs but gives wrong output]  
    ↓  
Check logic in `if/else` → conditions correct?  
    ↓  
Print debug values → `print(var)`  
    ↓  
✅ Expected Fix: Correct logic produces expected decision/output  

---

[While loop never ends]  
    ↓  
Check loop condition → does variable update each iteration?  
    ↓  
Add counter increment (`count += 1`)  
    ↓  
✅ Expected Fix: Loop ends when condition false  


### Session 12 – While Loops & Counters  

[Infinite loop in script]  
    ↓  
Check loop condition → `while attempt <= max_attempts`  
    ↓  
Confirm counter increment → `attempt += 1` inside loop  
    ↓  
If missing → add increment  
    ↓  
✅ Expected Fix: Loop ends correctly after max attempts.  

[Loop ends too soon]  
    ↓  
Print condition values each iteration  
    ↓  
Check logic: `<=` vs `<` vs `==`  
    ↓  
Adjust condition to match intended loop count  
    ↓  
✅ Expected Fix: Loop runs expected number of times.  

---

### Session 12.5 – Python Fundamentals Sandbox  

[IndentationError]  
    ↓  
Check alignment of loop/code blocks  
    ↓  
Correct indentation with 4 spaces per block  
    ↓  
✅ Expected Fix: Script runs without syntax errors.  

[Unexpected infinite loop]  
    ↓  
Inspect while loop condition  
    ↓  
Verify counter increments with `+= 1`  
    ↓  
✅ Expected Fix: Loop exits correctly after retries.  

[Logic error – break ends loop too soon]  
    ↓  
Review placement of `break` inside loop  
    ↓  
Move `break` only under correct success condition  
    ↓  
✅ Expected Fix: Loop retries until success or max attempts.  

[Summary counters incorrect]  
    ↓  
Check increments → `successes += 1`, `failures += 1`  
    ↓  
Ensure they’re updated in correct branch of logic  
    ↓  
✅ Expected Fix: End-of-run summary matches reality.  


### Session 13 – Collections (Lists, Dicts, Sets)  

[KeyError when accessing dict]  
    ↓  
Check if key exists → `if "R3" in device_ips:`  
    ↓  
Or use `.get("R3")` with default  
    ↓  
✅ Expected Fix: No crash when key missing.  

[Unexpected missing VLANs]  
    ↓  
Confirm sets defined correctly → required vs configured  
    ↓  
Verify use of `.difference()` vs `.intersection()`  
    ↓  
✅ Expected Fix: VLAN compliance check correct.  

[Unhashable type error in set]  
    ↓  
Check what’s inside set → only ints/strings allowed  
    ↓  
Avoid lists/dicts inside sets  
    ↓  
✅ Expected Fix: Set operations work as expected.  


## 2️⃣ `notes/cheatsheet.md` Update  

```markdown
## 🔹 Session 14 – File I/O (Configs & Logs)  
*(See: [Session 14 Notes](session_14.md))*  

| Command / Concept | Description | Expected Result |  
|-------------------|-------------|-----------------|  
| `open("file","r")` | Open file for reading | Returns file handle |  
| `f.read()` | Read entire file | String of contents |  
| `f.readlines()` | Read all lines | List of strings |  
| `open("file","w")` | Open for writing (overwrite) | File replaced |  
| `open("file","a")` | Open for appending | Data added at end |  
| `with open(...) as f:` | Context manager | File auto-closed | 

### Session 15 – YAML & JSON Conversion  

[Cannot import PyYAML]  
    ↓  
pip install pyyaml  
    ↓  
✅ Expected Fix: YAML scripts run successfully  

[JSON Decode Error]  
    ↓  
Check file syntax or encoding  
    ↓  
Use `json.load()` inside try/except  
    ↓  
✅ Expected Fix: File loads without errors  

[File not found on read]  
    ↓  
Confirm relative path (`labs/…` vs `scripts/…`)  
    ↓  
✅ Expected Fix: Script locates and reads file successfully  

### Session 16 – NX-API (NX-OS)

[401 Unauthorized]
    ↓
Verify Quick Access creds → export NXOS_USER/NXOS_PASS
    ↓
Re-run request
    ↓
✅ Expected Fix: HTTP 200 with JSON body

[KeyError parsing response]
    ↓
print(resp.text[:1000]) to inspect structure
    ↓
Adjust path: ins_api → outputs → output → body → TABLE_* → ROW_*
    ↓
✅ Expected Fix: Parser finds rows successfully

[SSL certificate verify failed]
    ↓
Set verify=False for lab (only)
    ↓
✅ Expected Fix: HTTPS call succeeds

