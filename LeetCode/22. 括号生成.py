"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
 

"""

# # 我的题解 官方题解
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         couut_right = 0
#         res = []

#         def dfs(count_left, count_right, string):   # count_left 左括号剩余未使用数量
#             if count_left == 0 and count_right == 0:
#                 res.append(string)
#                 return 
#             if count_left > 0:
#                 dfs(count_left-1, count_right, string + '(')
#             if count_left < count_right :
#                 dfs(count_left, count_right-1, string + ')')
#             return 
#         dfs(n, n, "")
#         return res 

# 官方题解
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans
