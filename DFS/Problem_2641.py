# Definition for a binary tree node.
"""
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.

Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^4
"""

from typing import Optional, List
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        m = Counter()

        def get_sibling_sum(r, l):
            # r, l mean node and level, respectively.
            if not r:
                return

            m[l] += r.val
            get_sibling_sum(r.left, l + 1)
            get_sibling_sum(r.right, l + 1)

        get_sibling_sum(root, 0)

        def dfs1(r, l):
            # r, l, and curr mean root node, level, and current node respectively.
            sum_of_cousins = m[l + 1] - (r.left.val if r.left else 0) - (r.right.val if r.right else 0)

            if r.left:
                r.left.val = sum_of_cousins
                dfs1(r.left, l + 1)
            if r.right:
                r.right.val = sum_of_cousins
                dfs1(r.right, l + 1)
            return r

        root.val = 0
        return dfs1(root, 0)


# [0, 1, 2, 2, 1, 2]
# solver = Solution()
# root = TreeNode(5)
# root.left = TreeNode(4)
# root.right = TreeNode(9)
# root.right.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(10)
# solver.replaceValueInTree(root)
# print(root.val)
# print(root.right.val)
# print(root.left.val)
# print(root.right.right.val)
# print(root.left.left.val)
# print(root.left.right.val)
