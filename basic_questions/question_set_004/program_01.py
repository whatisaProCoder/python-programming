"""
Write a C program to take an integer as input from the user
and print all the positive even numbers upto that integer.
"""

n = int(input("Enter an integer : "))

print(f"Positive even numbers upto {n}...")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
