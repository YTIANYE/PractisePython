"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # 我的题解：
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         self.count = 0 
#         self.sum_val = 0 
#         def pre(root):
#             if root is None:
#                 return 
#             self.sum_val += root.val 
#             if self.sum_val == targetSum:
#                 self.count += 1
#             pre(root.left)
#             pre(root.right)
#             self.sum_val -= root.val 
        
#         def run(root):
#             if root is None:
#                 return 
#             pre(root) 
#             run(root.left)
#             run(root.right)
        
#         run(root)
#         return self.count

# 官方题解：dfs
# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> int:
#         def rootSum(root, targetSum):
#             if root is None:
#                 return 0

#             ret = 0
#             if root.val == targetSum:
#                 ret += 1

#             ret += rootSum(root.left, targetSum - root.val)
#             ret += rootSum(root.right, targetSum - root.val)
#             return ret
        
#         if root is None:
#             return 0
            
#         ret = rootSum(root, targetSum)
#         ret += self.pathSum(root.left, targetSum)
#         ret += self.pathSum(root.right, targetSum)
#         return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/path-sum-iii/solutions/1021296/lu-jing-zong-he-iii-by-leetcode-solution-z9td/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 我实现的官方题解：前缀和
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1
        self.res = 0
        def dfs(root, curr):
            if root is None:
                return 
            curr += root.val 
            self.res += prefix[curr - targetSum]
            prefix[curr] += 1
            dfs(root.left, curr)
            dfs(root.right, curr)
            prefix[curr] -= 1
        dfs(root, 0)
        return self.res 
            
