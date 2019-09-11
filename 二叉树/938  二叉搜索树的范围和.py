""" 938. 二叉搜索树的范围和 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        if root is None:
            return None

        arr = []

        def preorder_travseral(root):
            arr.append(root.val)
            if root.left:
                preorder_travseral(root.left)
            if root.right:
                preorder_travseral(root.right)

        preorder_travseral(root)

        sum = 0
        for val in arr:
            if L <= val <= R:
               sum += val

        return sum


"""
思路：
    遍历一遍，然后过滤，累加
"""
