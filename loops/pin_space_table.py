# pin_space_table.py
# Calculate the time needed to try every possible PIN.

GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits

    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // (24 * 60)

    print(
        f"{digits} digits: {combinations} PINs, "
        f"{minutes} minutes, {days} days"
    )# pin_space_table.py
# Calculate the time needed to try every possible PIN.

GUESSES_PER_SECOND = 10

for digits in range(4, 9):
    combinations = 10 ** digits

    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // 60
    days = minutes // (24 * 60)

    print(
        f"{digits} digits: {combinations} PINs, "
        f"{minutes} minutes, {days} days"
    )