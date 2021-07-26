"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
"""
from random import randint

from tree import *


class Solution:
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了48.83%的用户
    内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.67%的用户
    """

    # 我的题解：递归
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        # 每次取数组中间值创建树节点， 两个的时候总是选择右边
        def func(nums):
            if nums is None:
                return None
            mid = int(len(nums) / 2)
            root = TreeNode(nums[mid])
            if nums[:mid]:
                root.left = func(nums[:mid])
            if nums[mid + 1:]:
                root.right = func(nums[mid + 1:])
            return root

        root = func(nums)
        return root

    # 官方题解
    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None
            # 选择任意一个中间位置数字作为根节点
            mid = (left + right + randint(0, 1)) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)


s = Solution()
nums = [-10, -3, 0, 5, 9]
# nums = [1, 3]
root = s.sortedArrayToBST(nums)
tree_print_graph(root)
