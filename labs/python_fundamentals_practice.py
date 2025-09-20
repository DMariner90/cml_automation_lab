###############################################
# counting with +=
###############################################
# Initialise a counter for failed SSH attempts.
failures = 0

# Simulate 3 login attempts.
for attempt in range(1, 4):  # Loops from 1->3
    failures += 1  # Increment the counter by 1.
    print(f"Attempt {attempt}: SSH failed (total failures = {failures})")
# Print the total number of failed attempts.

# Expected Result:
# Attempt 1: SSH failed (total failures = 1)
# Attempt 2: SSH failed (total failures = 2)
# Attempt 3: SSH failed (total failures = 3)

###############################################
## if/else logic
###############################################

device = "R1"

if device.startswith("R"):  # true if string starts with "R"
    print(f"{device} is a router")
else:
    print(f"{device} is not a router")

# Expected Result:
# R1 is a router


###############################################
## while loop with counter
###############################################

attempt = 1
max_attempts = 3


while attempt <= max_attempts:
    print(f"Attempt:{attempt}: Connecting....")
    attempt += 1  # incerment counter until it exceeds 3 -  max_attempts

# Expected Result:
# Attempt 1: Connecting....
# ...
# Attempt 3: Connecting....


###############################################
## for range in interfaces
###############################################

for i in range(1, 6):  # loop from 1 - 5
    print(f"Configuring Gig0/{i}")

# Expected Result:
# Congifuring Gig0/1
# Configuring Gig0/2
# ...
# Configuring Gig0/5

###############################################
## len() with device
###############################################

devices = ["R1", "SW1", "FW1"]

print(f"Total Devices: {len(devices)}")  # len() counts list elements

# Expected Results:
# Total Devices: 3

###############################################
## Function for reuseability
###############################################


def classify_device(name):
    if name.startswith("R"):
        return "Router"
    elif name.startswith("SW"):
        return "Switch"
    elif name.startswith("FW"):
        return "Firewall"
    else:
        return "Other"


# use function in a loop

for device in ["R1", "SW1", "FW1"]:
    print(f"{device} is a {classify_device(device)}")

# Expect Results:
# R1 is a Router
# SW1 is a Switch
# FW1 is a Firewall
