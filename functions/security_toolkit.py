MIN_LENGTH = 8


def border(width):
    """Print a border of + and dashes."""
    print("+" + "-" * (width + 2) + "+")


def show_box(text):
    """Print text inside a box."""
    border(len(text))
    print(f"| {text} |")
    border(len(text))


def show_menu():
    """Print the main menu."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):
    """Return the type of the port or 'invalid'."""
    if port < 0 or port > 65535:
        return "invalid"
    if port <= 1023:
        return "system"
    if port <= 49151:
        return "user"
    return "dynamic"


def check_port():
    """Ask for a port and show its range."""
    port = int(input("Port: "))
    result = port_range(port)
    show_box(f"Port {port}: {result}")


def password_problem(password, username):
    """Return the first problem found, or empty string."""
    if len(password) < MIN_LENGTH:
        return "too short"
    if password == username:
        return "same as the username"
    return ""


def check_password():
    """Ask username and password and show result."""
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password, username)
    if problem:
        show_box(f"Rejected: {problem}")
    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):
    """Calculate whole days needed to try every PIN."""
    total = 10 ** digits
    seconds = total // per_second
    return seconds // 86400


def check_pin():
    """Ask PIN digits and guesses per second, then show days."""
    digits = int(input("PIN digits: "))
    per_second = int(input("Guesses per second: "))
    days = days_to_guess(digits, per_second)
    show_box(f"{digits} digits: {days} days")


# ===== Main Program =====
show_menu()
checks = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")

    if choice == "1":
        check_port()
        checks += 1
    elif choice == "2":
        check_password()
        checks += 1
    elif choice == "3":
        check_pin()
        checks += 1
    elif choice == "q":
        show_box(f"Checks done: {checks}")
        break
    else:
        print("Unknown choice.")