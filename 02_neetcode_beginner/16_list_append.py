from typing import List


def append_to_list(my_list: List[int], elements: List[int]):
    for element in elements:
        my_list.append(element)
    return my_list


def pop_n_from_list(my_list: List[int], n: int):
    for _ in range(n):
        my_list.pop()
    return my_list


new_list = append_to_list([1, 2, 3], [5, 6, 7])
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.pop(1)
print(new_list)

new_list = append_to_list([1, 2, 3], [4, 5, 6])
print(pop_n_from_list(new_list, 2))
