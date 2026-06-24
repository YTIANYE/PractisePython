"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false
 

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def issame(p, q):
            if p is None and q is None:
                return True
            if p and q is None:
                return False 
            if q and p is None:
                return False 
            if p.val != q.val:
                return False
            return issame(p.left, q.right) and issame(p.right, q.left)

        return issame(root.left, root.right)
