# 📘 Session 7 – Linux Fundamentals Recap & Challenge Lab

**Topic:** Linux Fundamentals Recap & Challenge Lab  
**Milestone:** 1 – Linux & Server Fundamentals  

---

## 📝 What I Learned  
- Refreshed core Linux fundamentals: navigation, editing, ownership, permissions, processes, and services.  
- Understood why these basics are critical for automation workflows.  
- Practiced tying commands directly to automation relevance and troubleshooting.  

---

## 💻 Commands Practiced (with comments)  
```bash
pwd                                  # print working directory
mkdir recap_lab && cd recap_lab      # create sandbox and enter it
echo "demo" > file1.txt              # create test file
ls -l                                # list files with details
nano file1.txt                       # edit file interactively
cat file1.txt                        # display file content
less file1.txt                       # view with scrolling
sudo adduser testuser                # create new user
sudo usermod -aG sudo testuser       # add user to sudo group
groups testuser                      # check group membership
sudo chown $USER:$USER file2.txt     # set ownership
sudo chmod 640 file2.txt             # set restricted permissions
sleep 500 &                          # run process in background
ps aux | grep sleep                  # list & filter processes
kill <PID>                           # terminate process
sudo systemctl status ssh            # check SSH service
🔎 Review / Recap
What we practiced: navigation, editing, user/group creation, permissions, process management, and service checks.

Why it matters: most automation failures are due to permission or service issues; mastering these avoids wasted debugging.

Expected Outcomes: ability to create sudo users, assign permissions, and manage processes/services.

🧪 Challenge Lab(s) – Scenario & Tasks
Scenario: Onboard a new automation engineer with a secure Linux environment, including user access, workspace, script, SSH, and a shared lab directory.

Tasks:

Create user automation with sudo rights.

Create /opt/projects owned by automation, permissions 755.

Add run.sh printing "Automation Ready", executable by all.

Ensure SSH enabled and running.

Create /tmp/shared_lab with sticky bit.

Verify all steps.

Expected Outcome:

Automation user with sudo.

/opt/projects owned by automation, perms 755.

Script prints "Automation Ready".

SSH active and enabled.

Sticky bit on /tmp/shared_lab.

🆕 Challenge Lab Walkthrough (Answer)
Task 1 – Create user automation with sudo rights
bash
Copy code
sudo adduser automation
sudo usermod -aG sudo automation
groups automation
Expected Result: automation : automation sudo

Why: Service accounts shouldn’t use root but require controlled sudo escalation.

Task 2 – Create /opt/projects with correct perms
bash
Copy code
sudo mkdir -p /opt/projects
sudo chown automation:automation /opt/projects
sudo chmod 755 /opt/projects
ls -ld /opt/projects
Expected Result: drwxr-xr-x automation automation /opt/projects

Why: Gives automation user ownership, others safe access.

Task 3 – Add run.sh
bash
Copy code
echo -e '#!/bin/bash\necho "Automation Ready"' | sudo tee /opt/projects/run.sh
sudo chmod 755 /opt/projects/run.sh
su - automation -c "/opt/projects/run.sh"
Expected Result: Prints Automation Ready

Why: Confirms automation scripts run under the right user.

Task 4 – Ensure SSH enabled and running
bash
Copy code
sudo systemctl enable --now ssh
sudo systemctl status ssh
Expected Result: SSH status = active (running)

Why: Remote orchestration depends on SSH availability.

Task 5 – Create /tmp/shared_lab with sticky bit
bash
Copy code
sudo mkdir -p /tmp/shared_lab
sudo chmod 1777 /tmp/shared_lab
ls -ld /tmp/shared_lab
Expected Result: drwxrwxrwt

Why: Protects files in shared directories from deletion by others.

Cleanup:

bash
Copy code
sudo deluser automation
sudo rm -rf /home/automation /opt/projects /tmp/shared_lab
📚 Glossary
Term	Definition	Why it matters
Sticky Bit	Directory permission (t) preventing others deleting non-owned files.	Critical in shared labs like /tmp.
visudo	Safe sudoers editor with syntax check.	Prevents breaking sudo access.
systemctl	Service management tool.	Ensures automation-critical services like SSH run.
Octal Notation	Numeric permission notation (e.g., 755).	Used in automation scripts and playbooks.
