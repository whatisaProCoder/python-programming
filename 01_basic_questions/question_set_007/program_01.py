"""
Check whether the character entered through the
keyboard is a lowercase alphabet or upper case.
"""

character = input("Enter a character : ")[0]

if character.isalpha():
    if character.islower():
        print(f"{character} is lowercase alphabet")
    elif character.isupper():
        print(f"{character} is uppercase alphabet")
else:
    print(f"{character} is not an alphabet")
