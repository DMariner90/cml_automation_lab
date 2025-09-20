# Task 1


devices = ["R1", "SW1", "R2", "FW1", "R3"]
successes = 0

for device in devices:
    if device.startswith("R"):
        successes += 1
print(f"Routers found: {successes}")


# Task 2

# attempt = 0
attempt = 1
# max_attempts = 2
max_attempts = 3


while attempt <= max_attempts:
    if attempt == 2:
        print(f"Attempt: {attempt}: SSH success")
        break  # exit loop on success
    else:
        print(f"Attempt: {attempt}: SSH failed")
    attempt += 1  # increment attempt


# failures  = 0
# attempt == 2

# Simulate 3 login attempts.
# for attempt in range (1, 4): # Loops from 1->3
#    failures += 1 # Increment the counter by 1.
#    while attempt != 2:
#        print(f"Attempt {attempt}: SSH failed")
#        print(f"Attempt: {attempt}: SSH Success")


# Task 3

# for vlan in range(10, 16): # loop from 10 - 15
#    print(f"Creating vlan{vlan}")
