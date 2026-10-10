"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树

示例1:

输入:
    2
   / \
  1   3
输出: true
示例2:

输入:
    5
   / \
  1   4
    / \
   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。
"""
from tree import *

"""
注意只判断node.val > node.left.val 和 node.val < node.right.val 是够的
可能存在两种情况：
node.left.val 比 node的父亲节点值小， node是右孩子
node.right.val 比 node的父亲节点值大，node是左孩子
"""


class Solution:
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了97.46%的用户
    内存消耗：17.9 MB, 在所有 Python3 提交中击败了8.61%的用户
    """

    # 我的题解： 中序遍历, 验证遍历后得到的序列
    def isValidBST(self, root: TreeNode) -> bool:
        inorder_list = []

        # 中序遍历
        def inorder(root: TreeNode):
            if root is None:
                return
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)

        inorder(root)
        # print(inorder_list)
        # 验证是否平衡
        for i in range(len(inorder_list) - 1):
            if inorder_list[i] >= inorder_list[i + 1]:
                return False
        return True

    """
    执行用时：32 ms, 在所有 Python3 提交中击败了99.80%的用户
    内存消耗：17.1 MB, 在所有 Python3 提交中击败了71.19%的用户
    """
    # 官方题解：中序遍历, 遍历过程中进行比对
    """
    在中序遍历的时候实时检查当前节点的值是否大于前一个中序遍历到的节点的值
    一直遍历root.left, root = root.right, 继续一直遍历root.left
    """

    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        inorder = float('-inf')  # 记录前一个结点的值
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True


    """
    执行用时：44 ms, 在所有 Python3 提交中击败了93.26%的用户
    内存消耗：17.2 MB, 在所有 Python3 提交中击败了66.94%的用户
    """
    # 官方题解： 递归
    """
    判断子树中所有节点的值是否都在 (l,r)(l,r) 的范围内（注意是开区间）
    在递归调用左子树时，我们需要把上界 upper 改为 root.val
    同理递归调用右子树时，我们需要把下界 lower 改为 root.val
    """

    def isValidBST3(self, root: TreeNode) -> bool:
        def helper(root, lower, upper):
            if root is None:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            if not helper(root.left, lower, root.val):
                return False
            if not helper(root.right, root.val, upper):
                return False
            return True
        return helper(root, float('-inf'), float('inf'))


s = Solution()
# arr = [5, 1, 4, null, null, 3, 6]
arr = [2, 1, 3]
# arr = [5, 4, 6, null, null, 3, 7]
# arr = [2, 2, 2]
root = tree_create(arr, 0)
tree_print_graph(root)
print(s.isValidBST(root))
