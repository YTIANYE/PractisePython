"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

# 官方题解：动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:  
            for x in range(coin, amount + 1):   # 省去硬币初始赋值
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


# 我的题解：动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:  # 边界条件
            return 0
        res = amount
        nums = [-1] * (amount + 1)  # 达到该面额所需硬币数量
        for _, coin in enumerate(coins):
            if coin <= amount:
                nums[coin] = 1
        # print(nums)
        for i in range(1, amount + 1):
            if nums[i] == -1:
                continue
            for j, coin in enumerate(coins):
                index = i + coin
                if index > amount:
                    continue # 硬币无序，如果由小到大排列，可以break
                nums[index] = (
                    nums[i] + 1 if nums[index] == -1 else min(nums[i] + 1, nums[index])
                )
        return nums[-1]
