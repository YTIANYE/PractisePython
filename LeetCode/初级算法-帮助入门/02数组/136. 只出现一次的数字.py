"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

"""
from functools import reduce
from typing import List


class Solution:

    # 官方题解：数组中的全部元素的异或运算结果即为数组中只出现一次的数字。
    # 异或解决
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了60.42% 的用户
    内存消耗：16.6 MB, 在所有 Python3 提交中击败了18.81% 的用户
    """
    def singleNumber(self, nums: List[int]) -> int:

        return reduce(lambda x, y: x ^ y, nums)


    """
    执行用时：60 ms, 在所有 Python3 提交中击败了31.33% 的用户
    内存消耗：16.5 MB, 在所有 Python3 提交中击败了82.99% 的用户
    """
    def singleNumber1(self, nums: List[int]) -> int:
        # sorted(nums)  不正确
        nums.sort()
        # print("排序后的数组：" + str(nums))
        for i in range(0, len(nums), 2):
            if (i + 1) != len(nums):
                if nums[i] != nums[i + 1]:
                    return nums[i]
                else:
                    pass
            else:
                return nums[i]

    """
    执行用时：52 ms, 在所有 Python3 提交中击败了60.42% 的用户
    内存消耗：16.7 MB, 在所有 Python3 提交中击败了5.07% 的用户
    """

    def singleNumber2(self, nums: List[int]) -> int:

        return int(sum(set(nums)) * 2 - sum(nums))






li = [4,1,2,1,2]
# li = [2,2,1]
# li = [1, 0, 1]
s = Solution()
print(s.singleNumber(li))
