"""
Take a positive integer from the user. If it is even, print from
1 to that number. If it is odd, print in descending order starting
from that number and go to 1.
"""

number = int(input("Enter a positive integer : "))

if number < 1:
    print("Invalid number...")
    exit()

if number % 2 == 0:
    for i in range(1, number+1):
        print(f"{i} ", end="")
else:
    for i in range(number, 0, -1):
        print(f"{i} ", end="")
