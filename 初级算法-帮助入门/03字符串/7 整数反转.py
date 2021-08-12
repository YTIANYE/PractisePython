"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。


示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0
"""


class Solution:

    # 我的题解
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了91.74% 的用户
    内存消耗：14.5 MB, 在所有 Python3 提交中击败了98.83% 的用户
    """

    def reverse1(self, x: int) -> int:

        tag = 1
        if x == 0:
            return 0
        elif x < 0:
            tag = -1
            x *= tag
        num = 0
        while x != 0:
            num *= 10
            num += x % 10
            x = int(x // 10)
        num *= tag
        if (- 2147483648 ) <= num <= (2147483648 - 1):
            return num
        else:
            return 0

    # 官方题解
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了13.64% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了64.05% 的用户
    """

    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit

        return rev


s = Solution()
x = 1534236469
m = s.reverse(int(x))
print(m)

