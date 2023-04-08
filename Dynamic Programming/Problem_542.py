from typing import List

"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

"""


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # Diagonal direction is not allowed
        # termination condition : meet '0' component.
        result = [[0] * n for _ in range(m)]

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # 좌, 우, 상, 하

        def find_zero(i, j):
            if mat[i][j] == 0:
                return 0

        return result


solver = Solution()
print(solver.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(solver.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))