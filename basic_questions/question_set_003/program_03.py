# Write a program to swap two numbers without using 3rd variable.

x = int(input("Enter x : "))
y = int(input("Enter y : "))

x = x+y
y = x-y
x = x-y

print("\nAfter swapping...")
print(f"Value of x = {x}")
print(f"Value of y = {y}")
