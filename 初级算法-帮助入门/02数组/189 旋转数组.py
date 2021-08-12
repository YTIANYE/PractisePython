"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。



进阶：

    尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
    你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""
from typing import List


class Solution:

    """
    执行用时：56 ms, 在所有 Python3 提交中击败了25.60% 的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.34% 的用户
    """
    # 普通方法
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) == 0 or len(nums) == 1:
            return
        # arr = [] * k 这样的初始化，arr长度仍然为0 ，没有扩展
        k = k % len(nums) # 除去不必要的移动
        arr = [0] * k
        for i in range(0, k):
            arr[k - 1 - i] = nums[len(nums) - 1 - i]
        # 一定要从后往前复制， 不然会重复
        for i in range(len(nums)-k - 1, -1, -1):
                nums[i+k] = nums[i]
        for i in range(0, k):
            nums[i] = arr[i]
    # 数组翻转

    def rotate2(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[: k: -1]

        # 以下方式无效
        # nums[:k].reverse()
        # nums[k:].reverse()



s = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# nums = [1,2]
# k = 3

# s.rotate(nums, k)
# print(nums)
s.rotate2(nums, k)
print(nums)