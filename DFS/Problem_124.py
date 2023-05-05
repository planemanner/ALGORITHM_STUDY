"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.

A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""

from typing import Optional, List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total_sum = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        :param root:
        :return:
        """
        # Post-Order Traversal.
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # Basic case 나눔
            cases = [node.val,
                     node.val + left,
                     node.val + right,
                     node.val + left + right]

            self.total_sum = max(max(cases), self.total_sum)
            # 반환 대상 때문에 전체 트리값에 대한 반환 X 
            return max(cases[:3])

        dfs(root)

        return self.total_sum


class OptSolution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = -math.inf

        def DFS(node):
            nonlocal max_path
            if not node:
                return 0
            l = DFS(node.left)
            r = DFS(node.right)

            # 음수면 경로 선택 X
            if l < 0:
                l = 0
            if r < 0:
                r = 0

            max_path = max(max_path, node.val + l + r)

            return max(l + node.val, r + node.val)

        DFS(root)
        return max_path


# [-10,9,20,null,null,15,7]
# root = TreeNode(-10)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
#
# solver = Solution()
# print(solver.maxPathSum(root))

