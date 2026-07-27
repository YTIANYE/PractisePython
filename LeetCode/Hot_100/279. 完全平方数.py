"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

示例 1：

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
 
提示：

1 <= n <= 104
"""

# 我的题解：动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            if i * i > n:
                break 
            nums.append(i*i)
        # print(nums)
        count = [n] * (n+1)
        count[0] = 0
        count[1] = 1
        for i in range(1, n+1):
            # print("i: ", i)
            for _, num in enumerate(nums):
                k = i - num
                # print(num, k)
                if k < 0:
                    break 
                count[i] = min(count[k] + 1, count[i])
                # print(count)
        return count[-1]

        

# 我实现的官方题解：动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        count = [0] * (n+1)
        for i in range(1, n+1):
            j = 1
            min_count = n 
            while j * j <= i:
                min_count = min(min_count, count[i - j*j])
                j += 1
            count[i] = min_count + 1
                
        return count[-1]

        

        