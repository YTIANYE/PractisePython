# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from tree import *


class Solution:

    # 我的题解
    """
    执行用时：80 ms, 在所有 Python3 提交中击败了28.34%的用户
    内存消耗：19 MB, 在所有 Python3 提交中击败了11.59%的用户
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return

        # if p.val == root.val or q.val == root.val:
        #     return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
