"""
Print the following pattern with the number of rows taken from the user.
            1
          2 3 2
        3 4 5 4 3
      4 5 6 7 6 5 4
    5 6 7 8 9 8 7 6 5    
"""

rows = int(input("Enter number of rows : "))

for i in range(1, rows+1):
    for j in range(1, rows-i+1):
        print("  ", end="")
    for j in range(i, 2*i):
        print(f"{j} ", end="")
    for j in range(2*i-2, i-1, -1):
        print(f"{j} ", end="")
    print()
