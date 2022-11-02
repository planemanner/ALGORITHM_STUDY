"""
Given the root of a binary tree,

return the zigzag level order traversal of its nodes' values.

(i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -100 <= Node.val <= 100

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 같은 높이에 있는 지 판단하는 부분이 1개 필요하고
        # 순회하는 구문 1개가 필요하다.
        zigzag_list = []
        level = 0
        