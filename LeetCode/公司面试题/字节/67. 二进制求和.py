"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。

 

示例 1：

输入:a = "11", b = "1"
输出："100"
示例 2：

输入：a = "1010", b = "1011"
输出："10101"
 

提示：

1 <= a.length, b.length <= 104
a 和 b 仅由字符 '0' 或 '1' 组成
字符串如果不是 "0" ，就不含前导零
"""

# 我的题解：模拟 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        jin = 0
        i, j = len(a) - 1, len(b) - 1
        res = ""
        while jin != 0 or i >= 0 or j >= 0:
            numa = int(a[i]) if i >= 0 else 0
            numb = int(b[j]) if j >= 0 else 0
            i -= 1
            j -= 1
            he = numa + numb + jin
            res = str(he % 2) + res # 注意计算方式
            jin = 1 if he >= 2 else 0
        return res


# 官方题解：位运算
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


# 其他题解：禁止转换
class Solution:
    def addBinary(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2)) # :b 代表把十进制整数，格式化为二进制字符串。输出结果不带 0b 前缀，正好是题目要求。
