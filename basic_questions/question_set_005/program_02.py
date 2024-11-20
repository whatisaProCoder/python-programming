# Write a program to find out greatest among three numbers.

a, b, c = map(int, input("Enter three numbers : ").split())

greatest = None

if a > b and a > c:
    greatest = a
elif b > a and b > c:
    greatest = b
else:
    greatest = c

print(f"Greatest number = {greatest}")
