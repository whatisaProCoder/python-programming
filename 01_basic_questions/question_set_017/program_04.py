

def shift(x, y, z, n):
    for _ in range(n):
        x, y, z = z, x, y
    return x, y, z


if __name__ == "__main__":
    x, y, z = map(int, input("Enter three numbers : ").split())
    n = int(input("Enter number of right shifts: "))

    x, y, z = shift(x, y, z, n)

    print(f"After circular shifting {n} times...")
    print(f"x = {x}, y = {y}, z = {z}")
