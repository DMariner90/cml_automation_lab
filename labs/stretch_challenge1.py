# ----------------------------
# Stretch Challenge – Walkthrough
# Device classification + SSH retry simulation
# ----------------------------

devices = ["R1", "R2", "SW1", "SW2", "FW1"]  # Inventory of mixed device types

# Summary counters for final report
success_count = 0  # Tracks how many devices ultimately succeed
failure_count = 0  # Tracks how many devices ultimately fail


def classify_device(name: str) -> str:
    """Return a simple device type label from a hostname."""
    # If name starts with "R", treat as Router
    if name.startswith("R"):
        return "Router"
    # If name starts with "SW", treat as Switch
    elif name.startswith("SW"):
        return "Switch"
    # If name starts with "FW", treat as Firewall
    elif name.startswith("FW"):
        return "Firewall"
    # Otherwise a generic fallback
    else:
        return "Other"


def success_attempt_for(device_type: str) -> int | None:
    """
    Given a device type, return which attempt will succeed:
    - Routers succeed on attempt 1
    - Switches succeed on attempt 2
    - Firewalls never succeed (return None)
    """
    if device_type == "Router":
        return 1  # First try succeeds
    if device_type == "Switch":
        return 2  # Second try succeeds
    if device_type == "Firewall":
        return None  # Never succeeds within 3 tries
    return None  # Default: treat unknowns as never succeed


# Process each device one-by-one
for dev in devices:
    dev_type = classify_device(dev)  # Identify the device type
    success_on = success_attempt_for(
        dev_type
    )  # Determine which attempt (if any) will succeed

    attempt = 1  # Start at attempt 1
    max_attempts = 3  # We allow up to 3 attempts
    did_succeed = False  # Track if this device ever succeeded

    # Print a header for readability
    print(f"\n=== {dev} ({dev_type}) ===")  # Example: "=== R1 (Router) ==="

    # Retry loop
    while attempt <= max_attempts:  # Keep trying until we hit 3 attempts
        if success_on is not None and attempt == success_on:
            # This is the success attempt for this device type
            print(f"{dev} attempt {attempt}: SSH success")
            did_succeed = True  # Mark success
            break  # Stop retrying after success
        else:
            # Either this device has no planned success (Firewall),
            # or we haven’t reached the success attempt yet (Switch on attempt 1)
            print(f"{dev} attempt {attempt}: SSH fail")
            attempt += 1  # Increment the attempt counter with += 1

    # Update summary counters after attempts
    if did_succeed:
        success_count += 1  # += increments success tally by one
    else:
        failure_count += 1  # += increments failure tally by one

# Final summary line
print(f"\nSummary: {success_count} successes, {failure_count} failures")
