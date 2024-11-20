"""
Write a program to take 2 integers as input from user and print ->
    1. sum
    2. difference
    3. product
"""

print("Enter two numbers : ")
a, b = map(int, input("Enter two numbers: ").split())

sum = a+b
diff = a-b
prod = a*b

print(f"Sum = {sum}")
print(f"Difference = {diff}")
print(f"Product = {prod}")
