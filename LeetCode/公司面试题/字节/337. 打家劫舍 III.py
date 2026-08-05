"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。

除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

 

示例 1:



输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
示例 2:



输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
 

提示：

树的节点数在 [1, 104] 范围内
0 <= Node.val <= 104
"""

# 我实现的官方题解 ： 动态规划 + 后序遍历 + 哈希
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        f = {} # 偷
        g = {} # 不偷
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
            gl, gr, fl, fr = 0, 0, 0, 0 
            if root.left:
                gl = g[root.left] 
                fl = f[root.left]
            if root.right:
                gr = g[root.right]
                fr = f[root.right]
            f[root] = gl + gr + root.val    # 注意状态转移关系
            g[root] = max(fl, gl) + max(fr, gr)
        dfs(root)
        return max(f[root], g[root])

# 我实现的官方题解：动态规划 + 后序遍历 + 剪枝
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # f = {} # 偷
        # g = {} # 不偷
        def dfs(root):
            if not root:
                return 0, 0
            fl, gl = dfs(root.left)
            fr, gr = dfs(root.right)
            f = gl + gr + root.val    # 注意状态转移关系
            g = max(fl, gl) + max(fr, gr)
            return f, g
        f, g = dfs(root)
        return max(f, g)

        