"""
WAP to calculate the factorial of a given integer (>=0) using for loop.
factorial of n = n! = n*(n-1)*(n-2)*...2*1
For eg. 5! = 5*4*3*2*1 = 120
"""

n = int(input("Enter n : "))

if n < 0:
    print("Input is out of bounds.")
    exit()

fact = 1
for i in range(1, n+1):
    fact *= i

print(f"Factorial of {n} = {fact}")
