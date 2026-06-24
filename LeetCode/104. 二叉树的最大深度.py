"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

 

示例 1：



 

输入：root = [3,9,20,null,null,15,7]
输出：3
示例 2：

输入：root = [1,null,2]
输出：2
 

提示：

树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
 
面试中遇到过这道题?
1/5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 深度优先
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         self.res = 0 
#         def run(root, depth):
#             if root is None:
#                 return 
#             depth += 1
#             self.res = max(self.res, depth)
#             run(root.left, depth)
#             run(root.right, depth)
#         run(root, 0)
#         return self.res 
            
# 广度优先
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         res = 0 
#         if root is None:    # 注意判空
#             return res 
#         que = [root]
#         while que:
#             res += 1
#             q = que 
#             que = []
#             while q:
#                 node = q.pop(0)
#                 if node.left:
#                     que.append(node.left)
#                 if node.right:
#                     que.append(node.right)
#         return res 

# 官方题解
class Solution:
    def maxDepth(self, root):
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 
