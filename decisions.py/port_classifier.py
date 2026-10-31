# port_classifier.py

port = int(input("Enter port: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
elif port <= 1023:
    print("Range: system")
elif port <= 49151:
    print("Range: user")
else:
    print("Range: dynamic or private")

if 0 <= port <= 65535:
    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")