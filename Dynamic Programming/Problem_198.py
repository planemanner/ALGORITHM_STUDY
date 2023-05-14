"""
You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint stopping

you from robbing each of them is that adjacent houses have security systems connected

and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,

return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        total_houses = len(nums)
        if total_houses <= 2:
            return max(nums)

        maximum_robbing = [float("-inf") for _ in range(total_houses)]
        maximum_robbing[0] = nums[0]
        maximum_robbing[1] = max(nums[:2])

        def wis(i):

            if maximum_robbing[i] >= 0:
                return maximum_robbing[i]
            else:
                return max(wis(i-1), nums[i] + wis(i-2))

        for j in range(2, total_houses):
            maximum_robbing[j] = wis(j)

        return maximum_robbing[-1]


solver = Solution()
print(solver.rob([2, 7, 9, 3, 1]))  # 12
print(solver.rob([2, 1, 1, 2]))  # 4
