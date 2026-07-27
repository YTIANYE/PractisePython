"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

解释：

在 strs 中没有字符串可以通过重新排列来形成 "bat"。
字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
示例 2:

输入: strs = [""]

输出: [[""]]

示例 3:

输入: strs = ["a"]

输出: [["a"]]

 

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""

class Solution_1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i, s in enumerate(strs):
            li = [0]*26
            for zimu in s:
                li[ord(zimu) - ord('a')] += 1
            key = tuple(li)
            if key not in mp:
                mp[key] = []
            mp[key].append(s)
        return list(mp.values())
    
class Solution_0:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            if key not in mp:
                mp[key] = [s]
            else :
                mp[key].append(s)
        return list(mp.values())
