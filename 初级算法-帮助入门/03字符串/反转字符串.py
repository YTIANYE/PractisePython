"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]

"""
from typing import List


class Solution:
    # 我的题解
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了58.68% 的用户
    内存消耗：19.1 MB, 在所有 Python3 提交中击败了56.41% 的用户
    """
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(0, l // 2):
            s[i], s[l - 1 - i] = s[l - 1 - i], s[i]


    # 我的题解
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了89.80% 的用户
    内存消耗：19 MB, 在所有 Python3 提交中击败了85.76% 的用户
    """
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

solution = Solution()
# s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
solution.reverseString(s)
print(s)