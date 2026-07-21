"""
给你一个字符串 s，找到 s 中最长的 回文 子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""

# 我的题解——中心扩展法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxlen = 1
        x = y = 0
        for i in range(n - 1):
            ch1, ch2 = s[i], s[i + 1]
            j = 0
            while i + j < n and i - j >= 0 and s[i + j] == s[i - j]:
                if maxlen < 1 + 2 * j:
                    x = i - j
                    y = i + j
                    maxlen = 1 + 2 * j
                j += 1
            j = 0
            if ch1 != ch2:
                continue
            while i + 1 + j < n and i - j >= 0 and s[i + 1 + j] == s[i - j]:
                if maxlen < 2 + 2 * j:
                    x = i - j
                    y = i + j + 1
                    maxlen = 2 + 2 * j
                j += 1
        return s[x : y + 1]


# 官方题解 ——马拉车算法
class Solution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        end, start = -1, 0
        s = '#' + '#'.join(list(s)) + '#'   # 注意方法：在字符串首尾添加特殊字符，避免边界判断
        arm_len = []
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i
                right = i + cur_arm_len
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len
        return s[start+1:end+1:2]
