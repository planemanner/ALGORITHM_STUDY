"""
There are n cities connected by some number of flights.

You are given an array flights where flights[i] = [from i, to i, price i]

indicates that there is a flight from city from i to city to i with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.

If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= from i, to i < n
from i != to i
1 <= price i <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst

"""
from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        :param n:
        :param flights:
        :param src:
        :param dst:
        :param k: stop 의 개수. 만약 k 가 src~dst 사이의 최소 노드 수와 같으면 Dijkstra ?
        :return:
        Q1. k=0인데 src 에서 dst 로 가는 방법이 없으면 ?
        """
        graph = {i: [] for i in range(n)}

        for flight in flights:
            src_node, tgt_node, price = flight
            graph[src_node] += [(tgt_node, price)]

        costs = [float("inf") for _ in range(n)]
        costs[src] = 0  # source node

        x = [(0, 0, src)]

        visited = set()
        while x:
            price, current_k, next_node = heapq.heappop(x)
            if next_node == dst:
                return price

            if (next_node, current_k) in visited or current_k > k:
                # 방문을 했거나, 제약 조건을 넘어 가는 경우
                continue

            visited.add((next_node, current_k))

            for t_n, t_price in graph[next_node]:
                # next_node : k 에 대한 제약 조건을 통과, 동시에 visited 에도 없음
                # 이 node 의 인접 노드를 추가 후, price 까지 update 해서 다음 방문 node 에 추가
                heapq.heappush(x, (price + t_price, current_k + 1, t_n))
        # 만약 다 방문했는데도 길이 없으면 -1 반환
        return -1


solver = Solution()
# print(solver.findCheapestPrice(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
#                                src=0, dst=3, k=1))  # 700
# print(solver.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))  # 200
# print(solver.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))  # 500
# print(solver.findCheapestPrice(n=2, flights=[[1, 0, 5]], src=0, dst=1, k=1))
print(solver.findCheapestPrice(n=4, flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1))