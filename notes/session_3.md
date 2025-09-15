# Session 3 – Sep 17, 2025
**Topic:** Users, Groups & Sudo  
**Milestone:** 1 – Linux & Server Fundamentals

## What I Learned
- Accounts live in `/etc/passwd`, groups in `/etc/group`; UIDs/GIDs identify them.
- Members of the `sudo` group can run any command with sudo (Ubuntu default).
- Use `visudo`/`/etc/sudoers.d/*` for safe, granular sudo rules.
- Permissions can be scoped to *specific commands* (principle of least privilege).

## Commands Practiced (commented)
whoami                      # current user
id                          # UID/GID and groups
cat /etc/passwd             # list users
cat /etc/group              # list groups
sudo adduser lablimited     # create a test user
sudo visudo -f /etc/sudoers.d/lablimited   # safe sudoers edit for one user
sudo chmod 0440 /etc/sudoers.d/lablimited  # required sudoers file perms
sudo -l                     # list allowed sudo commands
sudo apt-get update         # allowed example
sudo cat /etc/shadow        # blocked example
sudo rm /etc/sudoers.d/lablimited          # remove rule (cleanup)
sudo deluser --remove-home lablimited      # delete user (cleanup)

## Issues / Fixes
- N/A (note any prompts/errors you saw and how you resolved them)

## Next Steps
- File ownership & group ownership (`chown`, `chgrp`), directory recursion, and verifying with `ls -l`.

