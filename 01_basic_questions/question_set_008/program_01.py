# WAP to print if a number is prime or not.

num = int(input("Enter a number : "))

factors = 0

for i in range(1, num+1):
    if num % i == 0:
        factors += 1

if factors == 2:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
