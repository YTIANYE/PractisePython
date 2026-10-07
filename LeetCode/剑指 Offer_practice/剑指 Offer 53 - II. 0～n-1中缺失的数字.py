"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
from typing import List


class Solution:
    # 我的题解: 暴力解法
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了36.97%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了100.00%的用户
    """

    def missingNumber1(self, nums: List[int]) -> int:
        sum = len(nums)
        for i, num in enumerate(nums):
            sum += i - num
        return sum

    # 我的题解：二分法
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了95.56%的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了60.45%的用户
    """

    def missingNumber2(self, nums: List[int]) -> int:
        # 缺失的是最后一个数时特殊判断一下
        if nums[-1] == len(nums) - 1:
            return len(nums)

        def bianary(nums, left, right):
            if left == right:
                return left

            mid = int((left + right) / 2)
            if nums[mid] == mid:
                left = mid + 1
                return bianary(nums, left, right)
            else:
                right = mid  # 为了记住第一个不等的位置
                return bianary(nums, left, right)

        return bianary(nums, 0, len(nums) - 1)

    def missingNumber3(self, nums: List[int]) -> int:
        # # 缺失的是最后一个数时特殊判断一下
        # if nums[-1] == len(nums) - 1:
        #     return len(nums)

        def bianary(nums, left, right):
            if left + 1 == right:
                if right == nums[right]:
                    return right + 1
                else:
                    return right

            mid = int((left + right) / 2)
            if nums[mid] == mid:
                left = mid  # left位置上的是相等的
                return bianary(nums, left, right)
            else:
                right = mid  # right位置上不等
                return bianary(nums, left, right)

        return bianary(nums, 0, len(nums) - 1)

    # 我实现的 官方题解：二分法
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == nums[mid]:
                left = mid + 1
                # 采用双指针而不是迭代，即使是缺失n的时候，
                # 也可以很简便的处理，不用单独的代码
            else:
                right = mid - 1
        return left

solu = Solution()

nums_arr = [[0],
            [0, 1, 2],
            [0, 1, 3],
            [0, 1, 2, 3, 4, 5, 6, 7, 9]]
for nums in nums_arr:
    print(solu.missingNumber(nums))
