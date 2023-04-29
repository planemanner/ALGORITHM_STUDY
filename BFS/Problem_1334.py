from typing import List
from collections import defaultdict
import heapq


class OptSolution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = [[] for _ in range(n)]
        available_city_list = [0 for _ in range(n)]

        for edge in edges:
            f, t, d = edge
            # Bidirectional
            graph[f].append([t, d])
            graph[t].append([f, d])

        for i in range(n):
            distances = [float('inf')] * n
            distances[i] = 0
            pq = [(0, i)]

            while pq:
                dist, node = heapq.heappop(pq)

                if dist > distanceThreshold:
                    break
                # dist => 누적거리
                if distances[node] < dist:
                    continue

                for neighbor, weight in graph[node]:
                    new_dist = dist + weight
                    # 이웃 노드까지 가는데 필요한 거리가 현재 누적거리보다 작다면 해당 거리를 업데이트 + 방문 목록에 추가
                    # 이게 Dijkstra Algorithm 의 Key Part.
                    if new_dist < distances[neighbor]:

                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            available_city_list[i] = sum(dist <= distanceThreshold for dist in distances) - 1

        min_value = min(available_city_list)
        max_id = 0

        for i in range(n):
            if available_city_list[i] == min_value:
                if i >= max_id:
                    max_id = i
        # print(available_city_list)
        return max_id


# solver = OptSolution()
#
#
# answer = solver.findTheCity(n=8,
#                             edges=[[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]],
#                             distanceThreshold=7937)  # Expected => 7
#
# print(answer)
