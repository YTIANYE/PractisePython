"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
 

示例 1：

输入：s = "()"

输出：true

示例 2：

输入：s = "()[]{}"

输出：true

示例 3：

输入：s = "(]"

输出：false

示例 4：

输入：s = "([])"

输出：true

示例 5：

输入：s = "([)]"

输出：false

 

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""

# # 我的题解
# class Solution:
#     def isValid(self, s: str) -> bool:
#         kuohao = []
#         for i in s:
#             if i == '(' or i == '{' or i == '[':
#                 kuohao.append(i)
#                 continue 
#             if len(kuohao) == 0:
#                 return False 
#             j = kuohao.pop()
#             new_str = j + i 
#             if not (new_str == "()" or new_str == "{}" or new_str == "[]"):
#                 return False 
#         if len(kuohao) != 0 :
#             return False 
#         return True 
                

# 官方题解
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack
