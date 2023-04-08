"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.

You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to.

More formally, for each v in graph[u], there is an undirected edge between node u and node v.

The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets
A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Constraints:

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        parent = [i for i in range(len(graph))]  # self parent

        def find_parent(u):
            if parent[u] == u:  # self parent
                return u
            # if not, find root until converge to self parent.
            return find_parent(parent[u])

        def union(u, v):
            # If u and v meet the condition to union, use this function.
            u_p = find_parent(u)
            v_p = find_parent(v)
            if u_p != v_p:
                parent[v_p] = u_p

        for i in range(len(graph)):
            p_i = find_parent(i)
            for j in graph[i]:
                if find_parent(j) == p_i:
                    # Since these nodes are adjacent, if those have same parent, it fails to make bipartite condition.
                    return False
                union(graph[i][0], j)
        return True


solver = Solution()
# print(solver.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))  # False
# print(solver.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))  # True
# print(solver.isBipartite([[4, 1], [2, 0], [3, 1], [4, 2], [0, 3]]))  # False
print(solver.isBipartite([[1], [0, 3], [3], [1, 2]]))  # True
print(solver.isBipartite([[3],[2,4],[1],[0,4],[1,3]]))  # True
print(solver.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
