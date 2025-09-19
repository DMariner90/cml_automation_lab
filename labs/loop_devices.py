devices = ["R1", "SW1", "FW1"]
MAX_ATTEMPTS = 3

for d in devices:
    print(f"\n=== Checking {d} ===")
    attempt = 1
    success = False

    while attempt <= MAX_ATTEMPTS:
        print(f"Attempt {attempt}: Pinging {d}...")
        # Simulated reachability rule: devices starting with "R" succeed
        if d.startswith("R"):
            print(f"✅ Device {d} reachable (on attempt {attempt})")
            success = True
            break
        attempt += 1

    if not success:
        print(f"❌ Device {d} unreachable after {MAX_ATTEMPTS} attempts")
