# Home Task 5 - Silver - Bug Hunt
# This program checks a connection against three rules
role = input("Role: ")
port = int(input("Port: ")) # Fix 1: runtime error - port was string, must be int
is_admin = role == "admin" # Fix 2: syntax error - was = instead of ==
is_system = port == 4432
is_web = port == 80 or port == 443 # Fix 3: logic error - (port == 80 or 443) always True
print(f"Role: {role}")
print(f"Admin: {is_admin}")
print(f"System port: {is_system}")
print(f"Web port: {is_web}") # Fix 4: syntax error - missing quote/brace
