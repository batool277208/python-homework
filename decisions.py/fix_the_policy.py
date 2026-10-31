# fix_the_policy.py

MIN_LENGTH = 12

username = input("Username: ")
password = input("New password: ")

if len(password) < MIN_LENGTH:  # syntax
    print("- Too short.")

if password == username:  # semantic
    print("- Same as the username.")

if len(password) >= 16:  # semantic
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength = "acceptable"
else:
    strength = "short"

print(f"Length: {len(password)} ({strength})")