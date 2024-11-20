# Write a program to find quotient and remainder of two numbers

x, y = map(float, input("Enter two numbers : ").split())

quotient = x / y
remainder = x % y

print(f"Quotient = {quotient}")
print(f"Remainder = {int(remainder)}")
