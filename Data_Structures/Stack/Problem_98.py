# LEETCODE 98

"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
"""

import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    pass


def compare_func(root_val, leaf_val, loc=None):
    if loc == 'left':
        if leaf_val < root_val:
            return True
        else:
            return False
    elif loc == 'right':
        if leaf_val > root_val:
            return True
        else:
            return False
    else:
        return True


def solution(root):
    # This solution only check an unit tree.
    # The constraints of this problem affect all subtrees.
    if not root:
        # Basic Case
        return True
    if root.left and root.val <= root.left.val:
        return False
    if root.right and root.val >= root.right.val:
        return False
    return solution(root.left) and solution(root.right)
"""
public boolean isValidBST(TreeNode root, Integer min, Integer max) {
    //1. Recursion - DFS
    if(root == null) return true;
    if(min != null && root.val <= min) return false;
    if(max != null && root.val >= max) return false;

    return isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max);
}

"""
sample = [5, 1, 4, None, None, 3, 6]
sample_2 = [5, 4, 6, None, None, 3, 7]
"""
             5
          4    6
             3   7        
             => 조상 노드까지 확인해야함.
             지금 이 
"""

root = TreeNode(val=5)
root.left = TreeNode(val=1)
root.right = TreeNode(val=4)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(val=3)
root.right.right = TreeNode(val=6)

root_2 = TreeNode(val=2)
root_2.left = TreeNode(val=1)
root_2.right = TreeNode(val=3)

root_3 = TreeNode(val=5)
root_3.left = TreeNode(val=4)
root_3.right = TreeNode(val=6)
root_3.left.left = None
root_3.left.right = None
root_3.right.left = TreeNode(val=3)
root_3.right.right = TreeNode(val=7)

print(solution(root))
print(solution(root_2))
