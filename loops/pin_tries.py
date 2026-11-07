# pin_tries.py
# Ask the user for a PIN and allow three tries.

MAX_TRIES = 3
CORRECT_PIN = "2580"

tries = 0

while tries < MAX_TRIES:
    pin = input("PIN: ")

    if pin == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        tries += 1
        print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}")

if tries == MAX_TRIES:
    print("Card blocked.")