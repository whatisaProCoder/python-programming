# Print even index (like 2, 4,...) values and print sum of these values.

a = [1, 2, 3, 4, 5, 6, 7, 8]
sz = len(a)

sum = 0
print("Even indexed values...")
for i in range(sz):
    if i % 2 == 0:
        print(f"{a[i]}")
        sum += a[i]

print(f"Sum = {sum}")
