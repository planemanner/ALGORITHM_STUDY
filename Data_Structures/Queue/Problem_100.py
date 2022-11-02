"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104

Example1
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example2
Input: p = [1,2], q = [1,null,2]
Output: false

Example3
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_binary_tree(node_list):
    def make_node(val, loc=None, root=None):
        if not root:
            return TreeNode(val=val)
        else:
            new_node = TreeNode(val=val)
            setattr(root, loc, new_node)
            return new_node
    idx = 0
    lv = math.log2(idx+1)
    root_node = None
    node_list = node_list[::-1]
    while node_list:
        node_val = node_list.pop()
        if idx == 0:
            cur_root = make_node(node_val)
            root_node = cur_root
            idx += 1
            continue
        elif idx % 2 == 0:
            loc = 'right'
            tmp_node = make_node(val=node_val, loc=loc, root=cur_root)
            idx += 1
        elif idx % 2 == 1:
            loc = 'left'
            tmp_node = make_node(val=node_val, loc=loc, root=cur_root)
            idx += 1

        if int(math.log2(idx)) > lv:
            cur_root = tmp_node

    return root_node


def preorder(root, node_list=[]):

    if root:
        # print(root.val)
        node_list.append(root.val)
        preorder(root.left)
        preorder(root.right)

    return node_list


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    node_list_1 = []
    node_list_2 = []

    def preorder(root, node_list):

        if root:
            node_list.append(root.val)
            preorder(root.left, node_list)
            preorder(root.right, node_list)
        else:
            node_list.append(root)
        return node_list

    tree_1 = preorder(p, node_list_1)
    tree_2 = preorder(q, node_list_2)

    if tree_1 == tree_2:
        return True
    else:
        return False


a = [1, 2]
b = [1, None, 2]
tree_1 = make_binary_tree(a)
tree_2 = make_binary_tree(b)

print(isSameTree(tree_1, tree_2))
