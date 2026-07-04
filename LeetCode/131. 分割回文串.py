"""
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
"""

# # 我的题解 归并
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         base = ['a'] * len(s)
#         for i in range(len(s)):
#             base[i] = s[i]
#         res.append(base.copy())
#         def find(base, index):  # index的作用，从上一次处理合并后的位置往后找继续能合并的，避免往前会重复，比如测试用例s ="cbbbcc"
#             for i in range(index, len(base)):
#                 if i+1 < len(base) and base[i] == base[i+1]:
#                     new_base = base.copy()
#                     new_base[i] = new_base[i] + new_base[i+1]
#                     new_base.pop(i+1)
#                     res.append(new_base.copy())
#                     find(new_base, i)
#                 if i - 1 >= 0 and i+1 < len(base) and base[i-1] == base[i+1]:
#                     new_base = base.copy()
#                     new_base[i-1] = new_base[i-1] + new_base[i] + new_base[i+1]
#                     new_base.pop(i+1)
#                     new_base.pop(i)
#                     res.append(new_base.copy())
#                     find(new_base, i-1)
#         find(base, 0)
#         return res 


# 我实现的官方题解 动态规划+递归
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        ans = []
        ishuiwen = [[True] * n for _ in range(n)]
        for i in range(n-1, -1, -1):    # 注意倒序
            for j in range(i+1, n):
                ishuiwen[i][j] = (s[i] == s[j]) and ishuiwen[i+1][j-1]

        def dfs(i):
            if i == n:  # 注意终止条件
                res.append(ans.copy())
                return 
            for j in range(i, n):
                if ishuiwen[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return res



            
