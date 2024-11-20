"""
Print the following pattern with the
number of rows taken from the user.
        *
       ***
      *****
     *******
    *********
"""

n = int(input("Enter number of rows : "))

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()
