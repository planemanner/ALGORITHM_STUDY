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


from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # Diagonal direction is not allowed
        # termination condition : meet '0' component.

        DIR = [0, 1, 0, -1, 0]  # => memory optimization

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:  # 일단 0 인 애들 다 넣기
                    q.append((r, c))
                else:  # 아닌 애들 이제 탐색할거 !
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()  # 0 인 애들에서 Pop 을 하네...?
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]  # Why ? 0, 1 / 1, 0 / 0, -1 / -1, 0
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1:
                    # Point 의 Validity Check
                    continue
                # Valid point r, c 에 대해
                mat[nr][nc] = mat[r][c] + 1  # 0 에서 1번 움직여야 하니까. 1 추가
                q.append((nr, nc))  # 이번 for 문에서 탐색한 친구이고 다음 대상 추가

        return mat


solver = Solution()
print(solver.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(solver.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))