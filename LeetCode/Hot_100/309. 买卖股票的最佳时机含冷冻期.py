"""
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
示例 2:

输入: prices = [1]
输出: 0
 

提示：

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

# 我实现的官方题解：动态规划
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp0 = [0] * n   # 手上有股票
        dp1 = [0] * n   # 手上没有股票，非冷冻期
        dp2 = [0] * n   # 手上有股票，冷冻期
        dp0[0] = -prices[0]
        for i in range(1, n):
            price = prices[i]
            dp0[i] = max(dp0[i-1], dp1[i-1] - price)
            dp1[i] = max(dp1[i-1], dp2[i-1])
            dp2[i] = dp0[i-1] + price 
        return max(dp0[-1], dp1[-1], dp2[-1])
        