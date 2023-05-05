"""
You are given a list of bombs.

The range of a bomb is defined as the area where its effect can be felt.

This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].

xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb.

When a bomb is detonated, it will detonate all bombs that lie in its range.

These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Example 1:


Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.
Example 2:


Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.
Example 3:


Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.


Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105

"""
from typing import List
from collections import defaultdict, deque
from math import sqrt


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        num_bombs = len(bombs)

        # 지금 이 Solution 은 BFS
        def detonation(src_x, src_y, src_r, tgt_x, tgt_y):
            xx = (src_x - tgt_x) ** 2
            yy = (src_y - tgt_y) ** 2
            dist = xx+yy

            if dist <= src_r ** 2:
                return True
            else:
                return False

        results = 0
        for i in range(num_bombs):
            detonatable = deque([i+1])
            current_result = 0
            visit = set()
            while detonatable:

                bomb_id = detonatable.pop()

                x, y, r = bombs[bomb_id-1]

                for j in range(num_bombs):
                    if j+1 in visit:
                        continue

                    t_x, t_y, t_r = bombs[j]

                    if detonation(x, y, r, t_x, t_y):
                        if j+1 not in visit:
                            detonatable.append(j+1)
                            current_result += 1
                            visit.add(j+1)

            if current_result > results:
                results = current_result

        return results


class Solution_DFS:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    curDis = sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
                    if r1 >= curDis:
                        adjList[i].append(j)

        mx_cnt = 0

        def dfs(node, visit):
            if node not in adjList:
                return 1

            curDepth = 1
            for child in adjList[node]:
                if child not in visit:
                    visit.add(child)
                    curDepth += dfs(child, visit)

            return curDepth

        for i in range(len(bombs)):
            visit = set()
            visit.add(i)
            mx_cnt = max(mx_cnt, dfs(i, visit))

        return mx_cnt

"""
이 문제는 DFS 로 푸는 게 맞다. 
BFS => O(N^3), 
DFS => O(N^2 * D), D 는 Traversal Depth D < N. 
Worst Case 의 경우 O(N^3) 이지만 일반적으로 BFS 보다 빠르다.
"""

solver = Solution_DFS()

print(solver.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))  # 5
print(solver.maximumDetonation([[1,1,5],[10,10,5]]))  # 1
print(solver.maximumDetonation([[2,1,3],[6,1,4]]))  # 2
# print(solver.maximumDetonation([[10000,10000,1000], [10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000]]))
# print(len([[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000],[10000,10000,1000]]))