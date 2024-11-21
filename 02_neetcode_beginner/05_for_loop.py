def one():
    for i in range(12+1):
        print(i)


def two():
    for i in range(2, 5):
        print(i)


def three():
    for i in range(1, 10+1, 2):
        print(i)


def four():
    for i in range(10, 0, -1):
        print(f"{i} ", end="")


def five():
    for i in reversed(range(10)):
        print(f"{i} ", end="")


def six():
    for i in reversed(range(10, 20+1)):
        print(f"{i} ", end="")


six()
