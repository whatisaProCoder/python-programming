""" 
Take an array of 10 numbers. Make a new
array by reversing the original array.
"""

sz = 10
a = []
print("Enter 10 numbers...")
a = list(map(int, input().split()))

b = []
for i in range(sz):
    b.append(a[sz-i-1])

print("Reversed array...")
for i in range(sz):
    print(f"{b[i]} ", end="")
