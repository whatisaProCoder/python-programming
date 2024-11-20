# WAP to display all the values in an array in reversed order.

a = [1, 2, 3, 4, 5]
size = len(a)

print("In reversed order...")
for i in range(size-1, -1, -1):
    print(f"{a[i]} ", end="")
