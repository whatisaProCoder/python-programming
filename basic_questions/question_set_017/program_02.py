""" 
Check whether a number can be expressed as the sum of two prime numbers.
"""


def is_prime(num):
    factors = 0
    for i in range(1, num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False


def sum_of_two_primes(num):
    for i in range(2, num):
        if is_prime(i) and is_prime(num-i):
            print(f"The prime numbers are {i} and {num-i}")
            print(f"Here, {i} + {num-i} = {num}")
            return
    print(f"{num} cannot be expressed as sum of two primes")


if __name__ == "__main__":
    num = int(input("Enter a number : "))
    sum_of_two_primes(num)
