# Take 5 float-numbers as input and find the average of them.

a, b, c, d, e = map(float, input("Enter 5 float-numbers : ").split())

average = (a+b+c+d+e)/5
print(f"Average = {average}")
