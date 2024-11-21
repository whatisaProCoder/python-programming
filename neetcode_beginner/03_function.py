def greet(name: str) -> None:
    print("Hello, " + name + "!")


def sum(x: int, y: int) -> int:
    return x + y


def get_name(name="Pritam Debnth"):
    print("Name is " + name)


greet("Pritam")
get_name("Ryan Renolds")
print(sum(2, 3))
