# labs/test_imports.py
"""
Session 9 – Python Virtual Environments & Package Management
Test script to verify key network automation libraries are installed.
"""

modules = ["requests", "netmiko", "ncclient"]

for m in modules:
    try:
        __import__(m)
        print(f"✅ Import successful: {m}")
    except ImportError:
        print(f"❌ Import failed: {m}")

print("\nEnvironment check complete.")
