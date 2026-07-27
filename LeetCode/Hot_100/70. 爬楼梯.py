"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
 

提示：

1 <= n <= 45
"""
# 官方题解：动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        p, q, r = 0, 0, 1
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q

        return r



# 我的题解 动态规划
import collections
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n 
        nums = [0] * n
        nums[0] = 1
        nums[1] = 2

        for i in range(2, n):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[-1]
        