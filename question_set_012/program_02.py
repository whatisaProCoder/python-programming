"""
WAP to print the first n numbers of the Fibonacci sequence.
Define the Fibonacci function and call it to print the numbers.
"""


def fibonacci_sequence(terms):
    a = 0
    b = 1
    c = None
    print(f"{terms} terms of Fibonacci Sequence...")
    for i in range(terms):
        c = a+b
        print(f"{a} ", end="")
        a = b
        b = c


if __name__ == "__main__":
    terms = int(input("Enter number of terms : "))
    fibonacci_sequence(terms)
