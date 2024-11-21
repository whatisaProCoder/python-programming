from typing import List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

length = len(numbers)

for i in range(length):
    print(f"{numbers[i]} ", end="")
print()

for number in numbers:
    print(f"{number} ", end="")
print()


def count_x(numbers: List[int], x: int) -> int:
    count = 0
    for number in numbers:
        if number == x:
            count += 1
    return count


print(count_x([1, 2, 3, 2, 2, 6, 7, 8], 2))
