"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
示例 2：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1
 

提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_0:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 叶子节点孩子为空
        if root is None:
            return None 
        # 找到目标节点
        if root.val == p.val or root.val == q.val:
            return root 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 找到公共祖先
        if left is not None and right is not None:
            return root
        # 左叶子结点不是祖先
        if left is None:
            return right 
        # 左叶子结点是祖先
        return left  


class Solution_1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 记录父节点
        # fa = dict()
        fa = {}
        def dfs(r):
            if r is None:
                return None
            if r.left is not None:
                fa[r.left] = r
                dfs(r.left)
            if r.right is not None:
                fa[r.right] = r
                dfs(r.right)
        dfs(root)

        # 最近公共祖先
        # l = list()
        l = []
        m = p
        while m is not None:
            l.append(m)
            m = fa.get(m)
        n = q
        while n is not None:
            if n in l :
                return n 
            n = fa.get(n)
        return n  


# 我的题解
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None 
        def dfs(root):
            flag = False 
            if root is None:
                return flag
            if root == p or root == q :
                flag = True
            left = dfs(root.left)
            right = dfs(root.right)
            if (flag and left) or (flag and right) or (left and right) :
                self.res = root 
            return flag or left or right    # 注意返回条件 or
        
        dfs(root)
        return self.res 

        