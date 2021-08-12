"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

"""
from typing import List


class Solution:
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了97.37%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.38%的用户
    执行用时：44 ms, 在所有 Python3 提交中击败了54.05%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了13.11%的用户
    """

    # 我的题解：纵向扫描
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs[0])):
            tag = True
            for j in range(len(strs)):
                # 注意判断长度
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    tag = False
                    break
            if tag:
                string += strs[0][i]
            else:
                break
        return string

    """
    执行用时：32 ms, 在所有 Python3 提交中击败了97.37%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了71.58%的用户
    """

    # 我的题解： 1的优化
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            tag = True
            for j in range(len(strs)):
                # 注意判断长度
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    tag = False
                    break
            if not tag:
                break
            i += 1
        return strs[0][:i]

    """
    执行用时：40 ms, 在所有 Python3 提交中击败了76.66%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了18.27%的用户
    """

    # 我的题解: 2的优化
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        i = 0
        while i < len(strs[0]):
            tag = True
            for j in range(len(strs)):
                # 注意判断长度
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
            i += 1
        return strs[0]

    # 官方题解：纵向扫描，与我的思路相同 2 的优化
    def longestCommonPrefix4(self, strs: List[str]) -> str:
        if not strs:
            return ""

        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]

    """
    执行用时：40 ms, 在所有 Python3 提交中击败了76.66%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.38%的用户
    """

    # 官方题解： 分治，横向
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start, end):
            if start == end:
                return strs[start]
            mid = (start + end) // 2
            # 最终得到两个字符串，而不是两组字符串
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            # 以下是重点操作
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)    # 左闭右闭


    # 官方题解： 二分法,纵向
    def longestCommonPrefix6(self, strs: List[str]) -> str:

        # 判断给定长度下，是否公共前缀
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


so = Solution()
strs = ["flower", "flow", "flight"]
# strs = ["flower", "flower", "flower", "flower"]
# strs = ["ab", "a"]
print(so.longestCommonPrefix(strs))
