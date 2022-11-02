"""
You are given an integer array nums.

You are initially positioned at the array's first index,

and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1)
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2)
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 105

"""
from typing import List


class Solution_1:
    def canJump(self, nums: List[int]) -> bool:
        """
        :param nums: the array represents your "maximum" jump length at that position.
        :return:
        BackTracking 은 이 문제에 부적합하다. 왜냐하면 Visit 여부를 체크하는 것 자체가 비효율적이기 때문
        이 문제는 Greedy Algorithm 이라기보다는 DP에 가까움.
        """
        pointer = 0
        reach = nums[pointer]
        goal_len = len(nums)
        if reach + 1 >= goal_len:
            return True

        while pointer < reach:
            pointer += 1
            # nums 에 접근하는 것 자체가 시간 소요함.
            reach = max(reach, pointer + nums[pointer])
            if reach + 1 >= goal_len:
                return True

        return False


class Solution_2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] >= target - i:
                target = i
        if target == 0:
            return True
        else:
            return False


solver = Solution_1()
print(solver.canJump([2,3,1,1,4]))
print(solver.canJump([3,2,1,0,4]))