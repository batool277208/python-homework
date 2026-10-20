#session timer 
session_seconds = int(input("session length in seconds:"))
minutes = session_seconds // 60
seconds = session_seconds % 60
print(f"Session length: {minutes} minutes and {seconds} seconds")

