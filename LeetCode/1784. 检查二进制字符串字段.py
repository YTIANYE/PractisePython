"""
1784. 检查二进制字符串字段
已解答
简单
相关标签
premium lock icon
相关企业
提示
给你一个二进制字符串 s ，该字符串 不含前导零 。

如果 s 包含 零个或一个由连续的 '1' 组成的字段 ，返回 true​​​ 。否则，返回 false 。

 

示例 1：

输入：s = "1001"
输出：false
解释：由连续若干个 '1' 组成的字段数量为 2，返回 false
示例 2：

输入：s = "110"
输出：true
 

提示：

1 <= s.length <= 100
s[i]​​​​ 为 '0' 或 '1'
s[0] 为 '1'
"""

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        l = len(s)
        last = "0"
        res = 0 
        for i in range(0, l):
            if s[i] == '1' and last == "0":
                res += 1 
            # elif s[i] == '0' and last == 0:
            #     pass
            # elif s[i] == '1' and last == 1:
            #     pass 
            # else:
            #     pass 
            last = s[i]
        print(res)
        return res < 2

    def checkOnesSegment_0(self, s: str) -> bool:
        return "01" not in s
        