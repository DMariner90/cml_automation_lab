## 📂 Repository Structure

This repo is organized to separate **learning labs** from **reusable scripts**:

- `labs/` → Hands-on exercises from sessions (sandbox files, challenge labs).  
  - These are practice-oriented and may be messy or experimental.  
  - Example: `labs/python_basics.py`  

- `scripts/` → Clean, reusable automation code.  
  - These scripts should be production-style or at least “ready-to-use.”  
  - Example (future): `scripts/push_config.py`  

- `notes/` → All session notes, cheat sheets, troubleshooting flows, and screenshots.  

- `configs/` → Config templates and device configurations used in labs.  

- `milestone_X_*` → Milestone-specific references and summaries.  

- `requirements.txt` → Python dependency lock file (kept updated via `pip freeze`).  

---

### 🧑‍💻 Workflow

1. Use **VS Code** (`code .`) for editing Python scripts and notes.  
2. Store quick experiments in `labs/`.  
3. Move polished, reusable tools into `scripts/`.  
4. Run scripts via terminal (WSL or NUC):  
   ```bash
   python labs/device_info.py
   python scripts/my_tool.py
