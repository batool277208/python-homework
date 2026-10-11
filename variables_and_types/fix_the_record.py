# fix_the_record.py
# This program prints a short record about a network device
device_name = "edge-router"
# Naming error: variable names cannot start with a number
backup_ip = "192.0.2.1"
# Naming error: class is a reserved keyword
device_type = "router"
# Type conversion error: "22" must contain digits
port = int("22")
print("Device:", device_name)
print("Backup IP:", backup_ip)
print("Type:", device_type)
print("Port:", port)