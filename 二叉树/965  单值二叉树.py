""" 965. 单值二叉树 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        if root is None:
            return False

        first = set()
        first.add(root.val)

        def preorder_travseral(root):
            first.add(root.val)
            if root.left:
                preorder_travseral(root.left)
            if root.right:
                preorder_travseral(root.right)

        preorder_travseral(root)
        return len(first) == 1
"""
思路：
    很简单 遍历一遍，去重集合
"""
