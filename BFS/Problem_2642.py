"""
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1.

The edges of the graph are initially represented by the given array edges where edges[i] = [from i, to i, edgeCost i]

meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].

It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2.
If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.

Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.

KEY CONSTRAINTS
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
"""
from typing import List
from collections import defaultdict
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        # Directed Graph.
        self.graph = defaultdict(list)
        self.n = n
        for edge in edges:
            self.addEdge(edge)

    def addEdge(self, edge: List[int]) -> None:
        """
        addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost].
        :param edge:
        :return:
        """
        src, tgt, cost = edge
        self.graph[src] += [(cost, tgt)]

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = [float("inf") for _ in range(self.n)]
        distances[node1] = 0
        search_targets = [(0, node1)]

        while search_targets:
            cur_cost, cur_node = heapq.heappop(search_targets)

            if distances[cur_node] < cur_cost:
                continue

            neighbors = self.graph[cur_node]

            for neighbor in neighbors:
                t_cost, t_node = neighbor
                comp_cost = t_cost + cur_cost
                if comp_cost < distances[t_node]:
                    distances[t_node] = comp_cost
                    heapq.heappush(search_targets, (comp_cost, t_node))

        return distances[node2] if distances[node2] != float("inf") else -1


g = Graph(n=4, edges=[[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(g.shortestPath(3, 2))
print(g.shortestPath(0, 3))
g.addEdge([1, 3, 4])
print(g.shortestPath(0, 3))
