"""
Given an array of integers nums which is sorted in ascending order,

and an integer target, write a function to search target in nums.

If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1)
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2)
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(array, low_idx, high_idx, tgt):
            mid = (low_idx + high_idx) // 2
            # Validity Check
            if high_idx >= low_idx:
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    return binary_search(array, low_idx, mid-1, tgt)
                else:
                    return binary_search(array, mid + 1, high_idx, tgt)
            else:
                return -1

        return binary_search(array=nums, low_idx=0, high_idx=len(nums)-1, tgt=target)


class Solution_2:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


solver = Solution()
print(solver.search([-1, 0, 3, 5, 9, 12], 9))
print(solver.search([-1, 0, 3, 5, 9, 12], 2))