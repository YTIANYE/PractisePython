""""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
 

提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅由小写英文字母组成
wordDict 中的所有字符串 互不相同
"""

# 我的题解——动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordLen = []  # 存放每个word的长度
        for word in wordDict:
            wordLen.append(len(word))
        n = len(s)
        tags = [0] * (n + 1)
        tags[0] = 1
        left = 0
        right = 1  # 左闭右开
        while left < n and left < right:
            if tags[left] != 0:
                for i in range(left, right):
                    if tags[i] == 0:
                        continue
                    for j in range(len(wordDict)):
                        l = wordLen[j]
                        # print("left:", left, "right:", right, "i:", i, "j:", j, "l:", l)
                        if i + l <= n and s[i : i + l] == wordDict[j]:
                            tags[i + l] = 1
                            right = max(right, i + l + 1)
                        # print("tags:", tags)
            left += 1
        return tags[-1] == 1

# 我实现的官方题解——动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True 
        for i in range(1, n+1): # 注意边界条件
            for j in range(i):
                dp[i] = dp[j] and s[j:i] in wordSet
                if dp[i]:
                    break 
        return dp[-1]
        
