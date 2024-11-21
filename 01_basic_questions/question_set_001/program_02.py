# Write a program to take an integer input from the user and print ->
#      1. its square
#      2. previous integer
#      3. next integer

n = int(input("Enter an integer : "))

sqr = n*n
pint = n-1
nint = n+1

print(f"Square : {sqr}")
print(f"Previous Integer : {pint}")
print(f"Next Integer : {nint}")
