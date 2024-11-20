""" 
WAP to count the total number of alphabets,
digits and special characters in string.
"""

alphabets, digits, special = 0, 0, 0

print("Enter a string...")
str = input()
size = len(str)

for i in range(size):
    ch = str[i]
    if not ch.isspace():
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1

print(f"No. of alphabets          : {alphabets}")
print(f"       digits             : {digits}")
print(f"       special characters : {special}")
