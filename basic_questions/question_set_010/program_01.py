"""
WAP to print the following pattern:
    1
    12
    123
    1234
    12345
"""

n = int(input("Enter n : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{j}", end="")
    print()
