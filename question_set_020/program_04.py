""" 
Declare an array of size 10. Take elements from the keyboard.
Delete the element from a position (taken from user) and print the final array.
"""

sz = 10
a = []
print("Enter 10 numbers...")
a = list(map(int, input().split()))

pos = int(input("Enter position to delete : "))

for i in range(pos-1, sz-1):
    a[i] = a[i+1]

sz -= 1

print("After deleting the element, the array...")
for i in range(sz):
    print(f"{a[i]} ", end="")
