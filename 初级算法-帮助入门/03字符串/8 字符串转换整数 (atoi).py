"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

    读入字符串并丢弃无用的前导空格
    检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
    返回整数作为最终结果。

注意：

    本题中的空白字符只包括空格字符 ' ' 。
    除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。



示例 1：

输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。

示例 2：

输入：s = "   -42"
输出：-42
解释：
第 1 步："   -42"（读入前导空格，但忽视掉）
            ^
第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   -42"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。

示例 3：

输入：s = "4193 with words"
输出：4193
解释：
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。

示例 4：

输入：s = "words and 987"
输出：0
解释：
第 1 步："words and 987"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："words and 987"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："words and 987"（由于当前字符 'w' 不是一个数字，所以读入停止）
         ^
解析得到整数 0 ，因为没有读入任何数字。
由于 0 在范围 [-231, 231 - 1] 内，最终结果为 0 。

示例 5：

输入：s = "-91283472332"
输出：-2147483648
解释：
第 1 步："-91283472332"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："-91283472332"（读入 '-' 字符，所以结果应该是负数）
          ^
第 3 步："-91283472332"（读入 "91283472332"）
                     ^
解析得到整数 -91283472332 。
由于 -91283472332 小于范围 [-231, 231 - 1] 的下界，最终结果被截断为 -231 = -2147483648 。



提示：

    0 <= s.length <= 200
    s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成

"""
import re

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton1:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_clo(self, c: str):
        if c.isspace():
            return 0
        # elif c == ('+' or '-'):       # 这样写不可以，因为 or前面的不为0，所以括号内的结果一直为‘+’
        elif c == '+' or c == '-':
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c: str):
        self.state = self.table[self.state][self.get_clo(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    # 我的题解
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了26.44% 的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了88.21% 的用户
    """

    def myAtoi1(self, s: str) -> int:
        maxn = 2 ** 31 - 1
        minn = -2 ** 31
        num = []
        change = False  # 记录符号是否改变
        sign = 1
        for i in range(len(s)):
            if s[i] == ' ' and len(num) == 0 and change == False:  # 前置空格
                continue
            elif 'A' <= s[i].upper() <= 'Z' or s[i] == '.' or s[i] == ' ':  # 结束条件
                break

            if s[i] == '-':
                if not num:  # num == []
                    if not change:  # 遇到的第一个符号
                        sign = -1
                        change = True
                    else:  # 第二次遇到符号，即s[i]前面有符号
                        return 0
                else:  # num != [],阿拉伯数字后面第一个是符号
                    break
            elif s[i] == '+':
                if not num:
                    if not change:
                        sign = 1
                        change = True
                    else:
                        return 0
                else:
                    break
            elif '0' <= s[i] <= '9':
                num.append(int(s[i]))
            else:
                break

        n = 0
        for i in num:
            n = n * 10 + i
        if sign == 1 and n > maxn:
            return maxn
        elif sign == -1 and n > -minn:
            return minn
        else:
            return n * sign

    # 我实现的官方题解
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了26.44% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了48.21% 的用户
    """

    def myAtoi2(self, s: str) -> int:
        automaton = Automaton1()
        for c in s:
            automaton.get(c)
        return automaton.sign * automaton.ans

    def myAtoi3(self, s: str) -> int:
        auto = Automaton()
        for c in s:
            auto.get(c)
        return auto.ans * auto.sign

    # 精选题解
    def myAtoi(self, s: str) -> int:
        """
        ^：匹配字符串开头
        [\+\-]：代表一个+字符或-字符
        ?：前面一个字符可有可无
        \d：一个数字
        +：前面一个字符的一个或多个
        \D：一个非数字字符
        *：前面一个字符的0个或多个
        """
        # 太简洁了，受不了了
        # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)

        # 分开写便于理解
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        s = s.lstrip()  # 去除左边多余空格
        num_re = re.compile(r'^[\+\-]?\d+')  # 设置正则规则
        num = num_re.findall(s)  # 查找匹配的内容
        num = int(*num)  # 由于返回的是一个列表，解包并且转换成整数
        return max(min(num, INT_MAX), INT_MIN)  # 返回值


sol = Solution()

# s = "42"
# s = "   -42"
# s = "4193 with words"
# s = "words and 987"
s = "-91283472332"
# s = "3.14159"
# s = "+-12"
# s = "-+12"
# s = "00000-42a1234"
# s = "-5-"
# s = "  -  413"
print(sol.myAtoi(s))
