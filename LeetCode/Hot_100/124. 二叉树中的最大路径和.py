"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 我的题解
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        def dfs(root):
            if root is None:
                return 0 
            left = dfs(root.left)
            right = dfs(root.right)
            temp = max(max(left + root.val, right + root.val), root.val)
            self.res = max(self.res, max(temp, left + right + root.val))    # 注意 left + right + root.val
            return temp 
        dfs(root)
        return self.res 
