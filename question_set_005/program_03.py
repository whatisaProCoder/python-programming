"""
Write a program to find the absolute value
of a number entered through the keyboard.
"""

number = int(input("Enter a number : "))

absolute_value = None

if number >= 0:
    absolute_value = number
else:
    absolute_value = -number

print(f"Absolute value of {number} is {absolute_value}")
