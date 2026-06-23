"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
"""
# 动态规划，时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]
            if nums[i] > res:
                res = nums[i]
        return res

class Status:
    def __init__(self, l_sum, r_sum, m_sum, i_sum):
        self.l_sum = l_sum
        self.r_sum = r_sum
        self.m_sum = m_sum
        self.i_sum = i_sum

