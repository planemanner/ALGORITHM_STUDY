"""
You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m * n)) time complexity
        # Binary Search

        row, col = len(matrix), len(matrix[0])
        # For vectorized representation
        left, right = 0, row * col - 1
        # Key condition. If right catch up with left or vice versa, it means that there is no target.
        while left <= right:
            mid = (left + right) // 2  # search mid
            num = matrix[mid // col][mid % col]  # index corresponding item
            if num == target:
                return True
            if num > target:
                # renew end point
                right = mid - 1
            else:
                # renew start point
                left = mid + 1
        return False


solver = Solution()
print(solver.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
print(solver.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13))
print(solver.searchMatrix(matrix=[[1,1]], target=2))
# print(solver.searchMatrix([[1, 3]], 3))