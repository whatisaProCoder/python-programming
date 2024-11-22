# set is unordered
# if order is important, then use a list
# set only stores unique elements
# set in python uses hashing

from typing import Set, List

my_set = {1, 2, 3}
print(my_set)

my_set = {3, 2, 1}
print(my_set)

b_set = set()

b_set.add(1)
b_set.add(2)
b_set.add(1)

print(b_set)


def list_to_set(nums: List[int]) -> Set[int]:
    my_set = set()
    for element in nums:
        my_set.add(element)
    return my_set


print(list_to_set([1, 2, 3, 4, 5, 5, 5, 6, 7, 7]))
