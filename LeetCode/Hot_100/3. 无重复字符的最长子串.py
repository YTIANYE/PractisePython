"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <2:
            return n 
        p, q = 0, 1
        res = 0 
        while q <= n-1:
            print(p, q)
            if s[q] in s[p:q]:
                for i in range(p, q):
                    if s[i] == s[q]:
                        p = i+1
                        res = max(res, q-i)
                        break
            q += 1
            res = max(res, q - p) # 注意右指针移动后计算长度
            
        return res 
                    
class Solution_0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0 
        jihe = set()
        q = 0
        for p in range(0, n): # 滑动窗口，每次移动左指针
            while q < n :
                if s[q] not in jihe:
                    jihe.add(s[q])
                    q += 1
                else:
                    jihe.remove(s[p])
                    break
            res = max(res, q - p)  # 注意位置不在else里
        return res 
                    

        

        