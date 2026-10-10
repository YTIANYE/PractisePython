"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:

输入: "race a car"
输出: false

"""
from builtins import str


class Solution:

    # 官方题解
    """
    方法一：筛选 + 判断
    最简单的方法是对字符串 sss 进行一次遍历，并将其中的字母和数字字符进行保留，放在另一个字符串 sgood 中。这样我们只需要判断 sgood 是否是一个普通的回文串即可。
    判断的方法有两种。第一种是使用语言中的字符串翻转 API 得到 sgood 的逆序字符串 sgood_rev，只要这两个字符串相同，那么 sgood 就是回文串。
    """
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了90.52% 的用户
    内存消耗：20.1 MB, 在所有 Python3 提交中击败了21.95% 的用户
    """
    def isPalindrome(self, s: str) -> bool:

        # isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
        sgood_rev = "".join(ch.lower() for ch in s if ch.isalnum())     # 这语句真棒  “”,join 值得学习，同时完成是不是数字或字母的判断和小写化
        return sgood_rev == sgood_rev[::-1]         # 这个正反比对太简洁了

    # 我的题解   相比之下 我的双指针 简直弱爆了
    """
    执行用时：56 ms, 在所有 Python3 提交中击败了69.11% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了79.25% 的用户
    """
    def isPalindrome4(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        # 注意忽略大小写    lower() 方法,返回将字符串中所有大写字符转换为小写后生成的字符串。

        new_s = s.lower()
        while i < j:
            # i 不在规定范围
            if new_s[i] == " " or (not('0' <= new_s[i] <= '9') and not('a' <= new_s[i] <= 'z')):
                i += 1
                continue
            # j 不在规定范围
            if new_s[j] == " " or (not('0' <= new_s[j] <= '9') and not('a' <= new_s[j] <= 'z')):
                j -= 1
                continue
            if new_s[i] == new_s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True     

        # 改进， 去掉声明新的字符串，没怎么节省空间,极大增加用时
        """
        执行用时：152 ms, 在所有 Python3 提交中击败了5.45% 的用户
        内存消耗：15 MB, 在所有 Python3 提交中击败了83.59% 的用户
        """
        """
        new_s = s.lower()
        while i < j:
            # i 不在规定范围
            if s[i].lower() == " " or (not('0' <= s[i].lower() <= '9') and not('a' <= s[i].lower() <= 'z')):
                i += 1
                continue
            # j 不在规定范围
            if s[j].lower() == " " or (not('0' <= s[j].lower() <= '9') and not('a' <= s[j].lower() <= 'z')):
                j -= 1
                continue
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
    
        """



s = Solution()
string = "A man, a plan, a canal: Panama"
# string = "0P"
# string = "race a car"
print(s.isPalindrome4(string))


