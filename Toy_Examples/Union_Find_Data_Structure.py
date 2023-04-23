"""
Union-Find 구조에 사용될 데이터 구조는 "참조" 가 가능한 구조여야 함.
가장 직관적으로 떠올리기 좋은 구조는 Tree.
근데 문제들을 보면 대게 list 구조를 쓰는듯 ?
=> 이는 O(N) 복잡도를 갖게 하므로, Tree 구조가 더 좋음 !

list 의 index 값을 원소 번호 그대로 대응 시키고, 값에 따라 function 내에서 Union 여부를 판단하는 식.
초기에는 본인이 root-node 가 되도록 설계

"""


class UnionFind:
    def __init__(self, data):
        # list 를 이용한 구현 예시
        self.parent_nodes = [i for i in range(len(data))]

    def find(self, cur_node):
        if self.parent_nodes[cur_node] == cur_node:
            return cur_node
        return self.find(self.parent_nodes[cur_node])

    def union(self, src_node, tgt_node):
        # 이 union 같은 경우 외부의 기준에 따라 합치면 된다.
        pivot_group_id = self.find(src_node)
        compare_group_id = self.find(tgt_node)
        if compare_group_id == pivot_group_id:
            return
        else:
            self.parent_nodes[tgt_node] = pivot_group_id


# Tree 를 쓸 때의 Union-Find 자료구조와 Path Compression by Rank 구현
# Union-Find 가 유의미하게 쓰이는 구조는 아래... 왜 ? Rank 에 기인한 O(logN) 복잡도 때문.
class ufds:
    parent_node = {}
    rank = {}

    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i
            self.rank[i] = 0

    def op_find(self, k):
        if self.parent_node[k] != k:
            self.parent_node[k] = self.op_find(self.parent_node[k])
        return self.parent_node[k]

    def op_union(self, a, b):
        x = self.op_find(a)
        y = self.op_find(b)

        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent_node[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent_node[x] = y
        else:
            self.parent_node[x] = y
            self.rank[y] = self.rank[y] + 1


from typing import List


def is_bipartite(n, dislikes: List[List[int]]):
    graph = {i: [] for i in range(n)}

    for relation in dislikes:
        ai, bi = relation[0] - 1, relation[1] - 1  # 0 부터 시작
        graph[ai] += [bi]

    colors = {}  # dictionary to store the color of each vertex
    queue = []  # queue for BFS

    # start BFS traversal from each uncolored vertex
    for vertex in graph:

        if vertex not in colors:
            colors[vertex] = 0  # assign color 0 to the first vertex
            queue.append(vertex)

            while queue:
                curr = queue.pop(0)  # remove and return the first element from the queue

                # check if the neighboring vertices have different color
                for neighbor in graph[curr]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[curr]  # assign opposite color to the neighboring vertex
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[curr]:
                        return False  # graph is not bipartite if two adjacent vertices have same color

    return True