# Write a program to swap two numbers using 3rd variable.

x = int(input("Enter x : "))
y = int(input("Enter y : "))

temp = x
x = y
y = temp

print("\nAfter swapping...")
print(f"Value of x = {x}")
print(f"Value of y = {y}")
