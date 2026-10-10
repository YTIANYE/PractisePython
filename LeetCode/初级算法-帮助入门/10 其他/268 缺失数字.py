"""
给定一个包含 [0, n]中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
nums 中的所有数字都 独一无二

进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
"""
from typing import List


class Solution:
    # 我的题解
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了29.91%的用户
    内存消耗：15.9 MB, 在所有 Python3 提交中击败了28.86%的用户
    """
    def missingNumber1(self, nums: List[int]) -> int:
        num = 0
        i = 0
        for n in nums:
            i += 1
            num += i - n
        return num

    # 我的题解
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了53.46%的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了81.85%的用户
    """
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i, n in enumerate(nums):
            i += 1
            num += i - n
        return num


s = Solution()
# nums = [3, 0, 1]
# nums = [0,1]
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# nums = [0]
print(s.missingNumber(nums))
