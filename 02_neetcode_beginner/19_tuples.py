from typing import Tuple

my_tuple = (4, 5, 6)
print(my_tuple)


for i in range(len(my_tuple)):
    print(f"{my_tuple[i]} ", end="")
print()

print(my_tuple[1:])

# raises an error
# my_tuple[0] = 1

print(f"Max : {max(my_tuple)}")
print(f"Min : {min(my_tuple)}")
print(f"Sum : {sum(my_tuple)}")


def create_pair(name: str, age: int) -> Tuple[str, int]:
    return (name, age)


print(create_pair("Alice", 25))
