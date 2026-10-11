# type_check.py
# This program checks and converts data types
# Predictions:
# 8080 is an int
# "8080" is a str
# 99.5 is a float
# "198.51.100.7" is a str
# 1_000 is an int
print(type(8080))
print(type("8080"))
print(type(99.5))
print(type("198.51.100.7"))
print(type(1_000))
converted_port = int("443")
converted_number = str(8080)
converted_decimal = float("2.5")
print(converted_port, type(converted_port))
print(converted_number, type(converted_number))
print(converted_decimal, type(converted_decimal))