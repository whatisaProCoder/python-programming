from typing import List

my_list = [1, 2, 3, 4, 5, 3]

print(my_list.index(3))


def find_index(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i


print(find_index(my_list, 3))
