print("Python sanbox Ready!")

device_name = "Router1"		# string
device_ip = "192.168.1.1" 	# string (IP stored as text)
port = 22 			# integer
is_reachable = True		# boolean

print(device_name, device_ip, port, is_reachable)

devices = ["Router1", "Switch1", "Firewall1"]		# list
credentials = {"user" : "admin", "pass" : "cisco"}	# dictionary

print(devices)
print(credentials)


username = input("Enter your name: ")
print(f"Hello, {username}! Welcome to the lab.")

