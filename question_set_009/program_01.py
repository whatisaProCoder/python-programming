"""
WAP in C to calculate addition, subtraction, multiplication of two integers
switch case taking option from the user.
If the user gives 1, addition will be performed.
If the user gives 2, subtraction will be performed.
If the user gives 3, multiplication will be performed.
"""

x, y = map(int, input("Enter two integers : ").split())

choice = int(input("Enter choice... 1 or 2 or 3 => "))

match choice:
    case 1:
        sum = x+y
        print(f"Summation = {sum}")
    case 2:
        diff = x-y
        print(f"Difference = {diff}")
    case 3:
        prod = x*y
        print(f"Product = {prod}")
    case _:
        print("Invalid choice...")
