"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

提示：你可以假定该字符串只包含小写字母。

"""
from builtins import str
from collections import Counter


class Solution:

    # 我的题解
    """
    执行用时：96 ms, 在所有 Python3 提交中击败了86.64% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了81.15% 的用户
    """
    def fristUniqChar(self, s: str) -> int:
        hashmap = Counter(s)
        # print(c)
        # for i in range(len(s)):
        #     if hashmap[s[i]] == 1:
        #         return i
        # 官方题解的写法
        # print(list(enumerate(s)))       # [(0, 'l'), (1, 'e'), (2, 'e'), (3, 't'), (4, 'c'), (5, 'o'), (6, 'd'), (7, 'e')]
        for i, ch in enumerate(s):      # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标,一般用在 for 循环当中
            if hashmap[ch] == 1:
                return i
        return -1


s = Solution()
# str = "loveleetcode"
str = "leetcode"
print(s.fristUniqChar(str))