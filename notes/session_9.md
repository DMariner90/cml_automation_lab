---

## 💻 Commands Practiced (with comments & expected results)  

```bash
python3 --version                           # check Python version → Python 3.x.x
pip3 --version                              # check pip version → pip x.x.x

python3 -m venv .venv                       # create venv → .venv/ created
source .venv/bin/activate                   # activate venv → prompt shows (.venv)
which python                                # confirm interpreter → .venv/bin/python

pip install requests netmiko ncclient       # install core packages → success logs
pip list                                    # list packages → requests, netmiko, ncclient shown

pip freeze > requirements.txt               # freeze dependencies → file created
cat requirements.txt                        # view versions → pinned versions shown

deactivate                                  # exit venv → prompt returns to normal
🔎 Review / Recap
Always use venvs to avoid polluting system Python.

Installed core libraries: requests, netmiko, ncclient.

Froze dependencies into requirements.txt.

Ran labs/test_imports.py to confirm environment readiness.

⚡ Troubleshooting
pip not found → sudo apt install python3-pip -y.

.venv not activating → run source .venv/bin/activate.

ImportError in script → pip install <missing-package>.

🧪 Challenge Lab
Created a second venv (automation_lab).

Installed requests, netmiko, ncclient.

Froze dependencies into requirements.txt.

Verified imports with labs/test_imports.py.

Cleaned up with rm -rf automation_lab.

💭 Last Thoughts
Virtual environments are critical for reproducible automation projects.

Most automation failures happen when dependencies aren’t managed.

Always activate the correct venv before running scripts.
