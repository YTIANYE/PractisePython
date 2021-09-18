"""
罗马数字包含以下七种字符:I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个罗马数字，将其转换成整数。输入确保在 1到 3999 的范围内。

"""
"""
示例1:

输入:"III"
输出: 3
示例2:

输入:"IV"
输出: 4
示例3:

输入:"IX"
输出: 9
示例4:

输入:"LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例5:

输入:"MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

提示：

1 <= s.length <= 15
s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
关于罗马数字的详尽书写规则，可以参考 罗马数字 - Mathematics 。


"""


class Solution:
    # 我的题解：直接理解
    """
    执行用时：60 ms, 在所有 Python3 提交中击败了20.44%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.79%的用户
    """

    def romanToInt1(self, s: str) -> int:
        nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = {"I": ("V", "X"), "X": ("L", "C"), "C": ("D", "M")}

        sum = 0
        i = 0
        while i < len(s):
            if s[i] in num.keys() and i + 1 < len(s):  # 检查是不是两个字母构成一个数
                if s[i + 1] in num[s[i]]:  # 构成
                    sum += nums[s[i + 1]] - nums[s[i]]
                    i += 2
                    continue
            sum += nums[s[i]]
            i += 1
        return sum

    # 官方题解：
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了61.19%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了28.46%的用户
    """

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        sum = 0
        length = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i + 1 < length and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                sum -= value
            else:
                sum += value
        return sum


s = Solution()
# string = "III"    # 3
# string = "IV"     # 4
# string = "IX"       # 9
# string = "LVIII"    # 58
string = "MCMXCIV"
print(s.romanToInt(string))
