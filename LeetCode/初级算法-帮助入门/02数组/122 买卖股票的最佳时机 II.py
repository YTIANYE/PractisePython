"""
买卖股票的最佳时机 II

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""
from typing import List


class Solution:
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了99.27% 的用户
    内存消耗：15.4 MB, 在所有 Python3 提交中击败了95.50% 的用户
    """
    # 方法：贪心
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <2:
            return 0

        profit = 0
        for i in range(0, len(prices) - 1):
            # temp = prices[i+1] - prices[i]
            # if temp > 0:
            #     profit += temp
            profit += max(0, prices[i+1] - prices[i])
        return profit


s = Solution() # 注意实例化的时候类后面有()
prices = [7, 1, 5, 3, 6, 4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
profit = s.maxProfit(prices)
print(profit)