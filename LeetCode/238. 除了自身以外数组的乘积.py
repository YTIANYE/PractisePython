"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
 

提示：

2 <= nums.length <= 105
-30 <= nums[i] <= 30
输入 保证 数组 answer[i] 在  32 位 整数范围内
 

进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
"""

class Solution_0:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(n):
            if i - 1 >= 0:
                answer[i] = answer[i - 1] * nums[i - 1]
        print(answer)
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1] * n  # [:i]
        left = [1] * n  # [i+1:]
        answer = [1] * n
        for i in range(n):
            if i - 1 >=0:
                left[i] = left[i-1] * nums[i-1]
        print(left)
        for i in range(n-1, -1, -1):
            if i + 1 < n:
                right[i] = right[i+1] * nums[i+1]
        print(right)
        for i in range(n):
            answer[i] = left[i] * right[i] 
        return answer