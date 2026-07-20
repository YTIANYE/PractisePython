"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

 

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
"""

# 我实现的官方题解：栈

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 栈底元素，「最后一个没有被匹配的右括号的下标」，
        res = 0
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack.append(i)
                continue
            # ")"
            j = stack.pop()  # 始终有栈底元素
            if stack:
                res = max(res, i - stack[-1])   # # 注意和栈顶计算
            else:
                stack.append(i)
        return res

# 我实现的官方题解 正向、反向遍历
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        res = 0
        for i in range(n):
            ch = s[i]
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right + left)
            elif right > left:
                left = right = 0
        left = right = 0  # 注意清零
        for i in range(n - 1, -1, -1):
            ch = s[i]
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, right + left)
            elif left > right:
                left = right = 0
        return res

