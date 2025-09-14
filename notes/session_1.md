# Session 1 – Environment Setup

**Date:** 2025-09-14  
**Objective:** Set up development environment and link to GitHub for ENAUTO project.

---

## Steps Completed

1. **Created project folder structure**
   - Base folder: `cml_automation_lab/`
   - Subfolders: `configs/`, `labs/`, `notes/`
   - Files: `README.md`, `requirements.txt`

2. **Python virtual environment**
   - Created `.venv` with `python3 -m venv .venv`
   - Activated via `source .venv/bin/activate`

3. **Git & GitHub integration**
   - Generated SSH key with `ssh-keygen -t rsa -b 4096 -C "email"`
   - Added key to GitHub, tested with `ssh -T git@github.com`
   - Initialized Git repo (`git init`, `git branch -M main`)
   - Linked to GitHub (`git remote add origin ...`)
   - First commit and push

4. **.gitignore setup**
   - Added `.venv/` and Python cache files to `.gitignore`
   - Removed `.venv` from GitHub to keep repo clean

---

## Key Commands Used

```bash
tree -L 2                # visualize project structure
ssh-keygen -t rsa -b 4096 -C "email"
ssh -T git@github.com    # test GitHub SSH connection
git init && git branch -M main
git remote add origin git@github.com:DMariner90/cml_automation_lab.git
git add . && git commit -m "Initial project structure"
git push -u origin main

