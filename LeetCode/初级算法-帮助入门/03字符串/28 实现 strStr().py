"""
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。


示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0


提示：
    0 <= haystack.length, needle.length <= 5 * 104
    haystack 和 needle 仅由小写英文字符组成

"""


class Solution:

    # 我的题解
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了41.66% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了49.21% 的用户
    """

    def strStr1(self, haystack: str, needle: str) -> int:

        if len(needle) == 0:
            return 0
        # 注意考虑长度不满足时，直接不存在
        if len(needle) > len(haystack):
            return -1

        i = 0
        # 注意符号 <=
        while i <= len(haystack) - len(needle):      # 避免多余计算倒数len(needle)的部分，及后面数组越界
            if haystack[i] != needle[0]:
                i += 1
            else:
                j = 0
                while j < len(needle):
                    if needle[j] != haystack[i + j]:
                        i += 1
                        break
                    j += 1
                if j == len(needle):        # 判断是不是全部验证完needle
                    return i
        return -1

    # 直接调用函数
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了90.07% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了73.05% 的用户
    """
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # 官方题解 KMP算法
    """
    前缀：对于字符串 abcxxxxefg，我们称 abc 属于 abcxxxxefg 的某个前缀。
    后缀：对于字符串 abcxxxxefg，我们称 efg 属于 abcxxxxefg 的某个后缀。
    """

sol = Solution()
# haystack = "hello"
# needle = "ll"
# haystack = "aaaaa"
# needle = "bba"
# haystack = ""
# needle = ""
# haystack = "aaa"
# needle = "aaaa"
# haystack = ""
# needle = "a"
haystack = "mississippi"
needle = "issip"
# haystack = "mississippi"
# needle = "issipi"
# haystack = "a"
# needle = "a"



print(sol.strStr(haystack, needle))