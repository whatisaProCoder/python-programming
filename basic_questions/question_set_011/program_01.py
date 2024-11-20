"""
Take any positive number from the user and print
-> the sum of its digits
-> the number of its digits
"""

n = int(input("Enter a positive number : "))

if n < 1:
    print("Invalid number...")
    exit()

num_digits = 0
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    num_digits += 1
    n = n // 10

print(f"Number of digits = {num_digits}")
print(f"Sum of digits    = {sum_digits}")
