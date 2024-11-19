# Write a program to find addition of 2 numbers without using addition operator.

a, b = map(int, input("Enter two numbers : ").split())

addition = a-(-b)
print(f"Summation = {addition}")
