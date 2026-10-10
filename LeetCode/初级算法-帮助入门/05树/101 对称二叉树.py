"""
给定一个二叉树，检查它是否是镜像对称的。
例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


进阶：

你可以运用递归和迭代两种方法解决这个问题吗？

"""
from tree import *


class Solution:
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了51.91%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了67.32%的用户
    """

    # 我的题解： 递归
    # 先序遍历（父亲 左孩子 右孩子）和与其对称的先序遍历（父亲 右孩子 左孩子），比对结果是否相同
    def isSymmetric1(self, root: TreeNode) -> bool:
        # 我的方式
        # def search(left, right):
        #     if left is None and right is None:
        #         return True
        #     elif left is None and right is not None:
        #         return False
        #     elif right is None and left is not None:
        #         return False
        #     else:
        #         if left.val != right.val:
        #             return False
        #         else:
        #             return search(left.left, right.right) and search(left.right, right.left)
        # 官方题解中的方式
        def search(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and search(left.left, right.right) and search(left.right, right.left)
        return search(root, root)

    """
    执行用时：36 ms, 在所有 Python3 提交中击败了86.43%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了87.72%的用户
    """
    # 我的题解： 迭代
    # 层次遍历，比对每一层结果是否对称，
    # 注意空结点一定要用null补充，方便比对，下一层就不需要在null结点继续拓展了
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        # 我的方式
        # queue = [root]
        # while queue:
        #     vals = []  # 存放当前层的value
        #     next_queue = []
        #     for node in queue:
        #         vals.append(node.val)  # 注意这一语句放在判断前面而不是里面
        #         if node.val != 'null':
        #             next_queue.append(node.left if node.left else TreeNode('null'))
        #             next_queue.append(node.right if node.right else TreeNode('null'))
        #     if vals != vals[::-1]:
        #         return False
        #     queue = next_queue
        # 官方题解的方式
        queue = [root, root]
        while queue:
            left = queue.pop()
            right = queue.pop()
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)

        return True


s = Solution()
arr = [1, 2, 2, 3, 4, 4, 3]
# arr = [1, 2, 2, null, 3, null, 3]
# arr = [1, 2, 2, 2, null, 2]
# arr = [1, 0]
# arr = [3, 67, 67, 18, null, null, 18, -1, -64, -64, -1, null, 61, -20, null, null, -20, null, 61]
root = tree_create(arr, 0)
tree_print_graph(root)
print(s.isSymmetric(root))
