"""
A wiggle sequence is a sequence where the differences between successive numbers

strictly alternate between positive and negative.

The first difference (if one exists) may be either positive or negative.

A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.

The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence,
leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List


class Solution:
    # Trash Code...
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n_num = len(nums)

        if n_num == 1:
            return 1
        if n_num == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1

        result = 0
        start_idx = 1

        if nums[1] - nums[0] > 0:
            prev_sign = 1
            result += 1
        elif nums[1] - nums[0] < 0:
            prev_sign = -1
            result += 1
        else:
            prev_sign = 0
            if n_num > 3:
                for _id in range(1, n_num):
                    diff = nums[_id+1] - nums[_id]
                    start_idx += 1

                    if diff > 0:
                        prev_sign = 1
                        result += 1
                        break
                    elif diff < 0:

                        prev_sign = -1
                        result += 1
                        break
            elif n_num == 3:
                if nums[2] == nums[1]:
                    return 1
                else:
                    return 2

            if len(nums[2:]) == 0 and prev_sign == 0:

                return 1

        for i in range(start_idx, n_num-1):

            diff = nums[i+1] - nums[i]

            if diff * prev_sign < 0:
                result += 1

            if diff > 0:
                prev_sign = 1

            elif diff < 0:
                prev_sign = -1

        return result + 1


"""
Intuition
Approach
Check if the length of the input list nums is less than 2. If yes, return the length of nums. This is because a sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
n = len(nums)
if n < 2:
    return n
Initialize two variables max_len and last_wiggle to keep track of the length of the longest wiggle subsequence and the last wiggle direction, respectively. Set max_len to 1 because the first element of the input list is always included in the wiggle subsequence.
max_len = 1
last_wiggle = None
Loop through the input list nums starting from the second element (i = 1) until the end (i = n-1). For each iteration, calculate the difference between the current and previous element using the formula diff = nums[i] - nums[i-1].
for i in range(1, n):
    diff = nums[i] - nums[i-1]
If the difference diff is positive and the last wiggle direction last_wiggle was negative, or if the difference diff is negative and the last wiggle direction last_wiggle was positive, then we've found a new wiggle direction and can update the length of the longest wiggle subsequence max_len by adding 1. Update the last wiggle direction last_wiggle accordingly by setting it to 1 if diff is positive, and -1 otherwise.
if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
    max_len += 1
    last_wiggle = 1 if diff > 0 else -1
Return the final value of max_len as the length of the longest wiggle subsequence.
return max_len
Complexity
Time complexity:
74.22%

Space complexity:
97.92%

Code
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # Initialize variables to keep track of the length of the longest 
        # wiggle subsequence and the last wiggle direction
        max_len = 1
        last_wiggle = None
        
        for i in range(1, n):
            # Calculate the difference between the current and previous element
            diff = nums[i] - nums[i-1]
            # If the difference is positive and the last wiggle direction was negative
            # or the difference is negative and the last wiggle direction was positive,
            # then we've found a new wiggle direction and can update the length of the 
            # longest wiggle subsequence
            if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
                max_len += 1
                # Update the last wiggle direction
                last_wiggle = 1 if diff > 0 else -1
                
        return max_len

"""
solver = Solution()
# print(solver.wiggleMaxLength([300,98,285,312,312,365]))  # 3
# print(solver.wiggleMaxLength([1,7,4,9,2,5]))  # 6
# print(solver.wiggleMaxLength([6, 7, 0]))  # 3
# print(solver.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])) # 7
# print(solver.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))  # 2
# print(solver.wiggleMaxLength([2, 1]))  # 2
# print(solver.wiggleMaxLength([2,1,3])) # 3
# print(solver.wiggleMaxLength([2, 2, 1]))  # 2
# print(solver.wiggleMaxLength([2, 2]))  # 1
# print(solver.wiggleMaxLength([1, 2]))  # 2
# print(solver.wiggleMaxLength([2, 2, 3]))  # 2
# print(solver.wiggleMaxLength([3,3,3,2,5]))  # 3
# print(solver.wiggleMaxLength([1,1,7,4,9,2,5]))  # 6

