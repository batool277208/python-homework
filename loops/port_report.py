# port_report.py
# Classify ports according to IANA port ranges.

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"Start port: {start_port}")
print(f"End port: {end_port}")

checked = 0

for port in range(start_port, end_port + 1):
    if 0 <= port <= 1023:
        category = "system"
    elif 1024 <= port <= 49151:
        category = "user"
    else:
        category = "dynamic"

    print(f"{port}: {category}")
    checked += 1

print(f"Ports checked: {checked}")