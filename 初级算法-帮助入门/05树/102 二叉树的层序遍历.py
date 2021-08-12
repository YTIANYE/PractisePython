"""给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""
from tree import *


class Solution:
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了45.70%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了12.40%的用户
    """
    # 我的题解
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
            # 只是return的话，返回的是null
        queue = [root]
        trees = []
        while queue:
            tree = []
            for node in queue:
                tree.append(node.val)
            trees.append(tree)
            q = queue
            queue = []
            while q:
                node = q.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return trees


s = Solution()
arr = [3, 9, 20, null, null, 15, 7]
root = tree_create(arr, 0)
tree_print_graph(root)
print(s.levelOrder(root))
