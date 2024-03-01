"""
Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.

"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums) - 1
    nums = sorted([[nums[i], i] for i in range(len(nums))])
    print(nums)
    result = nums[i][0] + nums[j][0]
    print(result)
    while result != target:
        if result > target:
            j -= 1
        else:
            i += 1
        result = nums[i][0] + nums[j][0]
    return [nums[i][1], nums[j][1]]


nums = [3, 3]
target = 6

print(twoSum(nums, target))
