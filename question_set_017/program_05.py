# Calculate GCD of two +ve integers using recursion.

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input("Enter two +ve numbers : ").split())
    gcd = get_gcd(a, b)
    print(f"GCD of {a} and {b} = {gcd}")
