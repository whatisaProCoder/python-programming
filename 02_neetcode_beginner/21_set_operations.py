from typing import List, Set
my_list = [1, 2, 3, 3, 3, 4, 4, 5, 5]

my_set = set(my_list)
print(my_set)

new_list = list(my_set)
print(new_list)

animals = {"Cat", "Dog", "Mouse"}

contains_cat = "Cat" in animals    # True
contains_lion = "Lion" in animals  # False


def count_unique_words(words: List[str]) -> int:
    my_set = set(words)
    return len(my_set)


print(count_unique_words(["hello", "world", "hello", "goodbye"]))
