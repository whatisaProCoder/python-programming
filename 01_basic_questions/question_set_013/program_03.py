"""
Print the given pattern.
a
bb
ccc
dddd
eeeee
"""

rows = int(input("Enter number of rows : "))

character = 'a'

for i in range(rows):
    for j in range(i+1):
        print(f"{character}", end="")
    print()
    character = chr(ord(character) + 1)
