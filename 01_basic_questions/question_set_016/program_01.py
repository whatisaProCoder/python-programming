"""
WAP to define and call a function that takes two positive integers
N and R as input and returns the value of P(N,R), where P(N,R) is the
number of permutations of N objects taken R at a time.
"""


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def P(N, R):
    return fact(N)//fact(N-R)


if __name__ == "__main__":
    N, R = map(int, input("Enter N & R : ").split())
    NPR = P(N, R)
    print(f"{N}P{R} = {NPR}")
