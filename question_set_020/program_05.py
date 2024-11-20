# Find the maximum and minimum of all array elements and their positions.

a = [8, 7, 6, 1, 2, 3, 9, 5, 6, 7, 8]
sz = len(a)

max = a[0]
maxi = 0
min = a[0]
mini = 0

for i in range(sz):
    if a[i] > max:
        max = a[i]
        maxi = i
    if a[i] < min:
        min = a[i]
        mini = i

print(f"Max element : {max}, position : {maxi+1}")
print(f"Min element : {min}, position : {mini+1}")
