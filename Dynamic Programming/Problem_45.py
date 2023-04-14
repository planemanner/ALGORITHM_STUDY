"""
You are given a 0-indexed array of integers nums of length n.

You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i.

In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        last_idx = len(nums) - 1
        memo = [float("inf") for _ in range(last_idx + 1)]
        memo[last_idx] = 0  # 몇번 점프해야 마지막 까지 도달할 수 있는 지 저장

        for i in range(last_idx + 1):
            j = last_idx - i
            available_jump = nums[j]
            while available_jump > 0:
                if j + available_jump >= last_idx:
                    memo[j] = 1
                    available_jump = 0
                else:
                    memo[j] = min(memo[j], memo[j+available_jump] + 1)
                    available_jump -= 1

        return memo[0]


solver = Solution()
# print(solver.jump([2, 3, 1, 1, 4]))  # 2
"""
inf, inf, inf, inf, 0
inf, inf, inf, 1, 0
inf, inf, 2, 1, 0
inf, 1, 3, 1, 0
inf, 1, 3, 1, 0
inf, inf, inf, inf, 0
inf, inf, inf, inf, 0
"""
# print(solver.jump([2, 3, 0, 1, 4]))  # 2
print(solver.jump([1]))


class FasterSolution:

    def jump(self, nums: List[int]) -> int:

        min_jump = 0
        l = r = 0

        while r < len(nums) - 1:

            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            min_jump += 1

        return min_jump