"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        replace(old, new [, max])
        把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
        """

        return s.replace(" ", "%20")


so = Solution()
s = input("请输入要转化的字符串：")
print(so.replaceSpace(s))