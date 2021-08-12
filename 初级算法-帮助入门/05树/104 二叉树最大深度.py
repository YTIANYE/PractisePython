"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明:叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度3 。

"""
from tree import *


class Solution:
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了99.59%的用户
    内存消耗：16.7 MB, 在所有 Python3 提交中击败了23.89%的用户
    """
    # 我的题解: 深度优先 DFS
    def maxDepth1(self, root: TreeNode) -> int:
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    """
    执行用时：48 ms, 在所有 Python3 提交中击败了72.05%的用户
    内存消耗：16 MB, 在所有 Python3 提交中击败了80.44%的用户
    """
    # 我的题解： 层次遍历 BFS
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            q = []      # 包含下一层所有结点的队列
            while queue:
                node = queue.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
            queue = q
        return depth




s = Solution()
# arr = [3, 9, 20, null, null, 15, 7]
arr = [0, 1, 2, null, 4, 5, 6, null, null, 9]
root = tree_create(arr, 0)
tree_print_graph(root)
print("二叉树的最大深度：", s.maxDepth(root))
