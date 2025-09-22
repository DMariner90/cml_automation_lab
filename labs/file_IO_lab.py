# Lab 1: Reading from a file in read mode ("r") (router.cfg)

# Open file in read mode
with open("labs/router.cfg", "r") as f:   # , r = read mode and as f = assign the read in string as f
    config = f.read()                   # Read entire file as a string
    
print("Full Config:\n", config)

# Read line by line in the chosen file
with open("labs/router.cfg", "r") as file:
    config = file.readlines()
print("Config Lines:" , config)

print("----------- BREAK LINE --------------")


# Lab 2: Writing logs to a file

# Open file in write mode ("w" overwrites if it exists)
with open("labs/connection_log.txt", "w") as log_file:
    log_file.write("Connecting to R1... SUCCESS\n")
    log_file.write("Connecting to R2... FAILED\n")

print("Log written to labs/connection_log.txt")

print("----------- BREAK LINE --------------")

# Lab 3: Appending logs

# Open file in append mode ("a")
with open("labs/connection_log.txt", "a") as appended_logs:
    appended_logs.write("Connecting to Sw1... SUCCESS\n")
    appended_logs.write("Connecting to SW2... FAILURE\n")
print("More logs appended to labs/connection_log.txt file")

print("----------- BREAK LINE --------------")

# Lab 4: Context Managers

devices = ["R1", "R2", "SW1", "FW1"]

# Open file in append mode safely
with open("labs/connection_log.txt", "a") as f:
    for device in devices:
        f.write(f"Device {device} processed.\n")

print("Devices appened safely with context manager")