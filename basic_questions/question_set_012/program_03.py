"""
WAP to declare and use a function that reverses
an integer when it is passed as a parameter.
"""


def get_reverse(number):
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse*10 + digit
        number = number // 10
    return reverse


if __name__ == "__main__":
    number = int(input("Enter a number : "))
    reversed_number = get_reverse(number)
    print(f"Reversed number = {reversed_number}")
