"""
给定一个整数，写一个函数来判断它是否是 3的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

示例 1：

输入：n = 27
输出：true
示例 2：

输入：n = 0
输出：false
示例 3：

输入：n = 9
输出：true
示例 4：

输入：n = 45
输出：false

提示：

-231 <= n <= 231 - 1

进阶：
你能不使用循环或者递归来完成本题吗？
"""
import math
import sys


class Solution:
    # 我的题解: 迭代
    """
    执行用时：76 ms, 在所有 Python3 提交中击败了70.86%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了34.92%的用户
    """

    def isPowerOfThree1(self, n: int) -> bool:
        i = 1
        while i:
            if n == i:
                return True
            elif i < n:
                i *= 3
            else:
                return False
    # 官方题解：迭代
    def isPowerOfThree3(self, n: int) -> bool:
        if n < 1:
            return False
        while (n % 3 == 0):
            n /= 3
        return n == 1

    # 我的题解：递归
    """
    执行用时：116 ms, 在所有 Python3 提交中击败了13.37%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.58%的用户
    """

    def isPowerOfThree2(self, n: int) -> bool:
        def fun(n):
            if n == 1:
                return True
            elif 1 < n < 3 or n == 0:
                return False
            else:
                return fun(n / 3)

        return fun(n)

    # 题解：对数
    """
    执行用时：72 ms, 在所有 Python3 提交中击败了78.31%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.48%的用户
    """

    def isPowerOfThree4(self, n: int) -> bool:
        # 注意 0 特殊处理
        if n <= 0:
            return False
        else:
            # num = math.log(n, 3)
            # return True if num == math.floor(num) else False

            e = math.log10(n) / math.log10(3)  # 为什么是这个
            return e == math.floor(e)

    # 官方题解
    """
    执行用时：64 ms, 在所有 Python3 提交中击败了92.24%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了83.13%的用户
    """
    def isPowerOfThree5(self, n: int) -> bool:
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(3)) % 1 == 0





s = Solution()
# n = 3
# n = 27
n = 45
# n = 243
print(s.isPowerOfThree(n))
