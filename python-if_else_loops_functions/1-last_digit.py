#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the last digit while preserving the sign
last_digit = abs(number) % 10
last_digit *= -1 if number < 0 else 1

output = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:
    output += " and is less than 6 and not 0"

print(output)