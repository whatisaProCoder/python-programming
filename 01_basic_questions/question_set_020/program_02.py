# Multiplication of odd index values.

a = [1, 2, 3, 4, 5, 6, 7, 8]
sz = len(a)

mult = 1
print("Odd indexed values...")
for i in range(sz):
    if i % 2 == 1:
        print(f"{a[i]}")
        mult *= a[i]

print(f"Product = {mult}")
