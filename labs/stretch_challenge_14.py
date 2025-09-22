"""  Stretch challenge 14:

Write a Python script that:

Reads the config file line by line.

Extracts any line starting with interface.

Writes them into labs/interfaces.txt.

"""

# Step 1: Read file in from router.cfg
with open("labs/router.cfg", "r") as cfg:
    lines = cfg.readlines()
    
# Keep only lines starting with "interface"
interfaces = [line.strip() for line in lines if line.strip().startswith("interface")]

print("Interfaces Found:", interfaces)

# Write extracted lines to interfaces.txt
with open("labs/interfaces.txt", "w") as extracted:
    for int in interfaces:
        extracted.write(int + "\n")

print(f"Interfaces {interfaces} saved to labs/interfaces.txt")