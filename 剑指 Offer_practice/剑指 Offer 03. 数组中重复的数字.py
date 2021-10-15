"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。
"""
from typing import List


class Solution:

    # 我的题解
    def findRepeatNumber(self, nums: List[int]) -> int:
        num_set = set()     # 注意空集合处理方式
        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return num
        return None

    def findRepeatNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            index = nums[i]
            if (0 == arr[index]):
                arr[index] += 1
            else:
                return index


solu = Solution()
nums = [2, 3, 1, 0, 2, 5, 3]
print(solu.findRepeatNumber(nums))