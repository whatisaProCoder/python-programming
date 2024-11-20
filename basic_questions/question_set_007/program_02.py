"""
WAP to check whether a character entered through the
keyboard is vowel or consonant or none of them.
"""

character = input("Enter a character : ")[0]

if character.isalpha():
    char = character.lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(f"{character} is a vowel")
    else:
        print(f"{character} is a consonant")
else:
    print(f"{character} is not an alphabet")
