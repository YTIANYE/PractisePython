"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false


示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

"""

class Soultion:

    """
    执行用时：32 ms, 在所有 Python3 提交中击败了72.39%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了22.59%的用户
    """
    # 我的题解
    def isValid(self, s: str) -> bool:
        # 如果字符串为奇数，直接排除
        if len(s) % 2 == 1:
            return False

        def isright(s1: str, s2: str) -> bool:
            return s1 + s2 == "()" or s1 + s2 == "[]" or s1 + s2 == "{}"
        stack = []
        left = ('(', '[', '{')
        for i in s:
            if i in left:
                stack.append(i)
            elif len(stack) != 0 and isright(stack[-1], i):
                stack.pop()     # stack.pop(-1)
            else:
                return False
        return len(stack) == 0      # 注意最后stack中不能有括号
        # return not stack


sou = Soultion()
# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([)]"
# s = "{[]}"
# s = "["
s = ']'
print(sou.isValid(s))




