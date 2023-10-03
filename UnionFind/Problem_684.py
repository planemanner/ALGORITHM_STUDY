"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.

The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge
between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List


class UnionFind:
    def __init__(self, n_nodes):
        self.parents = list(range(n_nodes))
        self.ranks = [0] * n_nodes

    def find(self, x):
        if x != self.parents[x]:
            # 자기 자신이 parent 가 아니면(즉, 더이상 부모 노드를 찾을 수 없고 본인이 최고 조상일 때) 현재 저장 되어 있는 부모 노드의 부모 노드를 찾는다.
            self.parents[x] = self.find(self.parents[x])
        # 이미 자기 자신이라면 그대로 리턴.
        return self.parents[x]

    def compression_find(self, x):
        # path compression
        if x == self.parents[x]:
            return x
        else:
            return self.compression_find(self.parents[x])

    def union(self, x, y):
        # always x < y
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return True

        if self.ranks[root_x] > self.ranks[root_y]:
            # rank 가 크면 클수록 Root 와 가깝다.
            self.parents[root_y] = self.parents[root_x]
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.parents[root_x] = self.parents[root_y]
        else:
            # rank 가 동일할 경우 node 의 순번이 작은 x 의 root node 를 root_y 의 parent node 에 할당한다.
            # why...?
            self.parents[root_y] = root_x
            self.ranks[root_x] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n_edges = len(edges)
        uf = UnionFind(n_edges + 1)

        for edge in edges:
            if uf.union(edge[0], edge[1]):
                return edge
