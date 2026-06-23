"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
 

提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

class Solution_0:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        res = []
        if lp > ls:
            return res 
        
        listp = [0] * 26
        lists = [0] * 26
        for i in range(lp):
            listp[ord(p[i]) -97] += 1   # 注意下标计算方式
            lists[ord(s[i]) -97] += 1
        if listp == lists:  # 列表支持等号比较
            res.append(0)
        
        for i in range(ls-lp):
            j = i + lp 
            if j < ls:
                lists[ord(s[i]) - 97] -= 1
                lists[ord(s[j]) - 97] += 1
            if listp == lists:
                res.append(i+1) # 注意添加i+1
        return res 


class Solution_1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def index(char):
            return ord(char) - 97

        ls = len(s)
        lp = len(p)
        res = []
        if lp > ls:
            return res 
        
        counts = [0] * 26
        for i in range(lp):
            counts[index(s[i])] += 1
            counts[index(p[i])] -= 1
        dif = 0 # 不同字母计数
        for i in range(len(counts)):
            if counts[i] != 0 :
                dif += 1
        if dif == 0:
            res.append(0)

        for i in range(ls - lp):
            j = i + lp 
            index_i = index(s[i])
            if counts[index_i] == 1:
                dif -= 1
            elif counts[index_i] == 0:
                dif += 1
            counts[index_i] -= 1

            index_j = index(s[j])
            if counts[index_j] == -1:
                dif -= 1
            elif counts[index_j] == 0:
                dif += 1
            counts[index_j] += 1
            if dif == 0:
                res.append(i+1)
        
        return res 