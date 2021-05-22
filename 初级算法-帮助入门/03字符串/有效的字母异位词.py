"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
如果两个单词字符串包含相同的字符及对应数量，只是字符顺序不同，则这两个单词就是有效的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true

示例 2:

输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""
from collections import Counter


class Solution:

    # 我的题解 哈希表
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了91.35% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.74% 的用户
    """
    def isAnagram(self, s: str, t: str):

        if len(s) != len(t):
            return False
        shashmap = Counter(s)
        thashmap = Counter(t)
        if len(shashmap) == len(thashmap):
            for i in shashmap.keys():
                if thashmap[i] != shashmap[i]:
                    return False
            return True
        else:
            return False

    # 哈希表，不用Counter函数
    """
    执行用时：60 ms, 在所有 Python3 提交中击败了62.19% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了64.80% 的用户
    """
    def isAnagram1(self, s: str, t: str):
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in t:
            if i in hashmap:
                hashmap[i] -= 1
            else:
                return False
        for i in hashmap.keys():
            if hashmap[i] != 0:
                return False
        return True

    # 排序
    """
    执行用时：68 ms, 在所有 Python3 提交中击败了31.51% 的用户
    内存消耗：15.6 MB, 在所有 Python3 提交中击败了15.34% 的用户
    """
    def isAnagram2(self, s: str, t: str):

        if len(s) != len(t):
            return False
        s_ = sorted(s)
        t_ = sorted(t)
        for i in range(len(s_)):
            if s_[i] != t_[i]:
                return False
        return True


solu = Solution()
s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
print(solu.isAnagram(s, t))
