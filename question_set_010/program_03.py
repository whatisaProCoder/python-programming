"""
WAP in C to take two integers as input from the user and
compute the LCM (lowest common multiple) of the two integers.
Use FOR loop.
"""

x, y = map(int, input("Enter two integers : ").split())

gcd = None

for i in range(1, x+1):
    if x % i == 0 and y % i == 0:
        gcd = i

lcm = int((x*y)/gcd)

print(f"LCM of {x} and {y} is {lcm}")
