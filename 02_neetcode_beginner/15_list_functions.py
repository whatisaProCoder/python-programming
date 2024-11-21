from typing import List


def get_sum(nums: List[int]) -> int:
    sum = 0
    for element in nums:
        sum += element
    return sum


def get_min(nums: List[int]) -> int:
    min = nums[0]
    for element in nums:
        if min > element:
            min = element
    return min


def get_max(nums: List[int]) -> int:
    max = nums[0]
    for element in nums:
        if element > max:
            max = element
    return max


nums = [1, 3, 2]
print(get_sum(nums))
print(get_min(nums))
print(get_max(nums))
