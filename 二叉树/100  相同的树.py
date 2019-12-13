""" 100. 相同的树 """


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        # P,Q 皆是 None
        if not p and not q:
            return True

        # P,Q 其中一方是 None
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
思路：
    同步的去比较每个节点
    1. 递归的去比较
    2. 层序遍历，再去具体去检查每一个节点

"""