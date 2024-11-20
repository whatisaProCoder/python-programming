"""
WAP to check whether a character entered through the
keyboard is alphabet, digit or special character.
"""

character = input("Enter a character : ")[0]

if character.isalpha():
    print(f"{character} is alphabet")
elif character.isdigit():
    print(f"{character} is digit")
else:
    print(f"{character} a special character")
