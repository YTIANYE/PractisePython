"""
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

测试用例保证答案唯一。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
 

进阶：你能设计一个在 O(m + n) 时间内解决此问题的算法吗？
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 边界
        ls = len(s)
        lt = len(t)
        if ls < lt:
            return ""

        def to_num(ch):
            num = ord(ch)
            if num >= 97:
                return num - 97  # 小写字母
            return num - 65 + 26  # 大写字母

        # 处理list_t
        list_t = [0] * 26 * 2
        for i in range(lt):
            index = to_num(t[i])
            list_t[index] += 1

        # 滑动窗口
        i, j = 0, 0  # [i,j)，j是开区间（因为j先自增）
        res = ""
        min_len = float("inf")  # 记录最小窗口长度
        count = lt
        while j < ls:
            index = to_num(s[j])
            if list_t[index] > 0:  # 注意判断条件，并且窗口中的数量还不够
                count -= 1
            list_t[index] -= 1  # 注意不在上面的if中
            j += 1
            # 匹配上了
            while count == 0:
                if j - i <= min_len:  # 注意min_len的作用
                    res = s[i:j]
                    min_len = j - i
                index_i = to_num(s[i])
                list_t[index_i] += 1
                if list_t[index_i] > 0:
                    count += 1
                i += 1
        return res
