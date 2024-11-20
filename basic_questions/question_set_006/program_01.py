"""
WAP to calculate the sum of first n positive integers
using for loop. Take the value of n as input from the user.    
"""

n = int(input("Enter n : "))

sum = 0

for i in range(1, n+1):
    sum += i

print(f"Sum = {sum}")
