from typing import List

my_list = [1, 2, 3, 4, 5]

print(my_list[1:3])
print(my_list[:3])
print(my_list[2:])
print(my_list[::-1])

print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


def get_last_three_elements(my_list: List[int]) -> List[int]:
    return my_list[len(my_list)-3:]
#   return my_list[-3:]


print(get_last_three_elements(my_list))
