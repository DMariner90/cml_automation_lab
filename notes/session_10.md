# 📘 Session 10 – Sep 24, 2025  
**Topic:** Python Basics – Variables, Data Types & Input/Output  
**Milestone:** 2 – Python for Network Automation  

---

## 📝 What I Learned  
- Variables store values such as device names, IPs, and ports.  
- Data types include strings, integers, booleans, lists, and dictionaries.  
- `print()` outputs data, `input()` collects user input.  
- F-strings provide clean, readable string formatting.  
- Sandbox scripts are useful for practicing and revision.  

---

## 💻 Commands Practiced (with comments & expected results)  

```bash
nano labs/python_basics.py                    # create sandbox file → editable file opened
python labs/python_basics.py                  # run script → prints "Python Sandbox Ready!"

# Variables
device_name = "Router1"                       # string → stores text
device_ip = "192.168.1.1"                     # string
port = 22                                     # integer
is_active = True                              # boolean
print(device_name, device_ip, port, is_active) # → Router1 192.168.1.1 22 True

# Lists & dictionaries
devices = ["Router1", "Switch1", "Firewall1"] # list → prints ['Router1','Switch1','Firewall1']
credentials = {"user": "admin", "pass": "cisco"} # dict → prints {'user':'admin','pass':'cisco'}

# Input/output
username = input("Enter your username: ")     # prompt user
print(f"Hello, {username}!")                  # → Hello david!
