from typing import List


# class Solution:
#     # Time limit exceeded
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#
#         def recur(i, j, path, visited):
#             if i == len(grid) - 1 and j == len(grid[0]) - 1:
#                 dist[0] = min(dist[0], path)
#             visited.append([i, j])
#             for k in range(i - 1, i + 2):
#                 for l in range(j - 1, j + 2):
#                     if k >= 0 and l >= 0 and k < len(grid) and l < len(grid[0]) and grid[k][l] == 0 and [k,
#                                                                                                          l] not in visited:
#                         if dist[0] == float('inf') or dist[0] > path + 1:
#                             recur(k, l, path + 1, visited)
#             visited.pop()
#
#         path, dist, visited = 1, [float('inf')], []
#         if not grid[0][0]:
#             recur(0, 0, path, visited)
#         return -1 if dist[0] == float('inf') else dist[0]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1

        Q = [(0, 0, 1)]
        # 최초로 end point 에 도달하는 경우에 가장 짧은 거리가 될 것이기 때문에. min 하는 과정이 필요 없다.
        while Q:
            i, j, path = Q.pop(0)
            if i == M - 1 and j == N - 1:
                return path
            if grid[i][j] == 0:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < M and 0 <= l < N and grid[k][l] == 0:
                            # Valid path check
                            Q.append((k, l, path + 1))
                grid[i][j] = 1  # visited, so mark as 1

        return -1


solver = Solution()
print(solver.shortestPathBinaryMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(solver.shortestPathBinaryMatrix([[0,0,1,1,0,0],[0,0,0,0,1,1],
                                       [1,0,1,1,0,0],[0,0,1,1,0,0],
                                       [0,0,0,0,0,0],[0,0,1,0,0,0]]))