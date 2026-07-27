"""
1758. 生成交替二进制字符串的最少操作数
已解答
简单
相关标签
premium lock icon
相关企业
提示
给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。

交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 "010" 是交替字符串，而字符串 "0100" 不是。

返回使 s 变成 交替字符串 所需的 最少 操作数。

 

示例 1：

输入：s = "0100"
输出：1
解释：如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。
示例 2：

输入：s = "10"
输出：0
解释：s 已经是交替字符串。
示例 3：

输入：s = "1111"
输出：2
解释：需要 2 步操作得到 "0101" 或 "1010" 。
 

提示：

1 <= s.length <= 104
s[i] 是 '0' 或 '1'
"""

class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)
        x = 0 # 1010
        y = 0 # 0101

        for i in range(0, l):
            if i % 2 == 0:
                if s[i] == "0":
                    x += 1
                else :
                    y += 1
            else:
                if s[i] == "0":
                    y += 1
                else :
                    x += 1
            print(x, y)

        return min(x, y)

class Solution_0:
    def minOperations(self, s: str) -> int:
        cnt = sum(int(c) != i % 2 for i, c in enumerate(s))
        return min(cnt, len(s) - cnt)

