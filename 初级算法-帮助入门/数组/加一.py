"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
    1 <= digits.length <= 100
    0 <= digits[i] <= 9

"""
from typing import List


class Solution:

    # 我的题解
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了83.27% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了72.63% 的用户
    """
    def plusOne1(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        l = len(digits)
        i = -1
        while digits[i] > 9:
            if i == (0 - l):
                for num in digits:
                    num = 0
                digits[0] = 1
                digits.append(0)
                break
            digits[i] -= 10
            i = i - 1
            digits[i] += 1
        return digits

    # 根据别人的思路写的题解
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了34.59% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了77.90% 的用户
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
            i -= 1
        # 99 情况的特殊处理
        digits[0] = 1
        digits.append(0)
        return digits

s = Solution()
# digits = [4,3,2,1]
digits = [9, 9]
print(s.plusOne(digits))