#!/usr/bin/python3
import random

# Generate a random signed number
number = random.randint(-10000, 10000)

# Determine the last digit
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Prepare the output message
output_message = f"Last digit of {number} is {last_digit} and is "

# Check conditions for the last digit
if last_digit > 5:
    output_message += "greater than 5"
elif last_digit == 0:
    output_message += "0"
else:
    output_message += "less than 6 and not 0"

# Print the final message
print(output_message)
