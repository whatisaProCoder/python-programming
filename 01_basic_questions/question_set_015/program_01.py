"""
Print the following pattern with the number of rows taken from the user.
    1 2 3 4 5 6 7 8
    *             *
    *             *
    *             *
    *             *
    *             *
    *             *
    1 2 3 4 5 6 7 8
"""

rows = int(input("Enter number of rows : "))

for i in range(1, rows+1):
    for j in range(1, rows+1):
        if i == 1 or i == rows:
            print(f"{j} ", end="")
        elif j == 1 or j == rows:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
