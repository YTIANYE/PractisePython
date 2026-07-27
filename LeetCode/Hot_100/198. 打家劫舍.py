"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

# 官方题解：动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[size - 1]
        
# 官方题解：动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second


# # 我的题解：动态规划
# # 与官方题解的不同在于，我遍历到当前房屋时，我假定一定偷当前房屋
# # 而官方题解遍历到当前房屋时，他假定截止当前房屋，能偷的最大金额
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         if n == 2:
#             return max(nums[0], nums[1])
#         if n == 3:
#             return max(nums[0] + nums[2], nums[1])
#         p, q, x, y = nums[0], nums[1], nums[2] + nums[0], 0 
#         for i in range(3, n):
#             print(p, q, x, y)
#             y = nums[i] + max(p, q)
#             p = q
#             q = x
#             x = y
#         return max(q, x)
        
        

        