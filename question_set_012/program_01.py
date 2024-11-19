"""
WAP to define a function that prints
the factorial of a given number.
"""


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(f"Factorial of {num} is {fact}")


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    factorial(num)
