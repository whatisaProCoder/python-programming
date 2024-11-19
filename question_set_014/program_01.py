"""
WAP to define a function that finds the
sum of all positive integers upto a given integer.
Define the function recursively.
"""


def sum(number):
    if number == 0:
        return 0
    else:
        return number+sum(number-1)


if __name__ == "__main__":
    number = int(input("Enter a integer : "))
    summation = sum(number)
    print(f"Summation = {summation}")
