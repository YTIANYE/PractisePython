"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

 

示例 1：


输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：

输入：root = [1,2]
输出：1
 

提示：

树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 我的题解：深度遍历
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.res = 0 
#         def deep(node):
#             if node is None:
#                 return -1
#             depth_left = deep(node.left)
#             depth_right = deep(node.right)
#             depth = max(depth_left, depth_right) + 1 
#             len_node = depth_left + 1 + depth_right + 1
#             self.res = max(self.res, len_node)
#             return depth
#         deep(root)
#         return self.res
    
# 评论题解
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0  # 全局变量，记录最大路径（直径）

        def dfs(node):
            if not node:
                return 0  # 空节点，深度0
            
            # 递归拿到左、右子树最大深度
            left = dfs(node.left)
            right = dfs(node.right)

            # 经过当前节点的最长路径 = 左深度 + 右深度
            self.max_len = max(self.max_len, left + right)

            # 向上一层返回当前子树的深度：左右更深的那一条 + 当前节点这条边
            return max(left, right) + 1

        dfs(root)
        return self.max_len

        

            
        