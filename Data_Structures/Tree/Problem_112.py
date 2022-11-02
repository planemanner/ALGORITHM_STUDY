"""
Given the root of a binary tree and an integer targetSum,

return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Example 1)
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2)
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3)
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # targetSum 에 이르는 경로가 있는 지 검사
        # preorder
        # 마지막 Node 에 닿으면 그 경로까지 이르는 데 모든 값의 합 계산
        if not root:
            return False

        p_sum = 0
        check = []

        def dfs(node, path_sum):
            path_sum += node.val
            if not (node.right or node.left) and path_sum == targetSum:
                check.append(True)
            if node.left:
                dfs(node.left, path_sum)
            if node.right:
                dfs(node.right, path_sum)

        dfs(root, p_sum)
        if len(check) != 0:
            return True
        else:
            return False


class Solution_2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs -> stack
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()

            if not node.left and not node.right and targetSum == total:
                return True

            if node.left:
                stack.append((node.left, total + node.left.val))
            if node.right:
                stack.append((node.right, total + node.right.val))

        return False


tree_1 = TreeNode(5)
tree_1.left = TreeNode(4)
tree_1.left.left = TreeNode(11)
tree_1.left.left.left = TreeNode(7)
tree_1.left.left.right = TreeNode(2)
tree_1.right = TreeNode(8)
tree_1.right.left = TreeNode(13)
tree_1.right.right = TreeNode(4)
tree_1.right.right.right = TreeNode(1)

tree_2 = TreeNode(1)
tree_2.left = TreeNode(2)
tree_2.right = TreeNode(3)

tree_3 = None


solver = Solution()
print("Case 1")
print(solver.hasPathSum(tree_1, 22))
print("Case 2")
print(solver.hasPathSum(tree_2, 5))
# print("Case 3")
# solver.hasPathSum(tree_3, 0)