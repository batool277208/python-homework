# fix_the_stats.py
# Count failed logins and calculate the average session length.

events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

failed = 0

for event in events:
    if event == "FAILED":
        failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0

for value in minutes:
    if value > 0:
        total += value
        count += 1

average = total / count

print(f"Average session: {average} minutes")

for level in range(1, 5):
    print(f"Level {level}")