from typing import List


def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


print(runningSum([3,1,2,10,1]))
