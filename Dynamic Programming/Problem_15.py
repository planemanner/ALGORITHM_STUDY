"""
Given an integer array nums,

return all the triplets [nums[i], nums[j], nums[k]]

such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array_len = len(nums)
        if array_len == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
