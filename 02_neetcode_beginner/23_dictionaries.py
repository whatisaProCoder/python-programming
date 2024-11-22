from typing import Dict
from typing import List


def frequency_numbers(numbers: List[int]) -> None:
    hashmap = {}
    for number in numbers:
        if number in hashmap:
            hashmap[number] += 1
        else:
            hashmap[number] = 1
    for key, value in hashmap.items():
        print(f"Value : {key}, Frequency : {value}")


numbers = [1, 2, 3, 3, 4, 4, 5, 5, 5, 2, 1]
frequency_numbers(numbers)


def create_dict(name: str, age: int) -> Dict[str, int]:
    dict = {}
    dict[name] = age
    return dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    dict = {}
    for i in range(len(words)):
        dict[words[i]] = i
    return dict


print(create_dict("Alice", 25))
print(list_to_dict(["Keyboard", "Mouse", "Monitor", "Harddisk"]))
