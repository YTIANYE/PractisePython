"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

示例 1：

输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false
调用 isBadVersion(5)-> true
调用 isBadVersion(4)-> true
所以，4 是第一个错误的版本。
示例 2：

输入：n = 1, bad = 1
输出：1

提示：

1 <= bad <= n <= 231 - 1

"""


class Solution:
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了81.44%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了51.85%的用户
    """

    # 我的题解：二分法、递归
    def firstBadVersion1(self, n):

        def binarySearch(left, right):
            mid = int((left + right) / 2)
            if isBadVersion(mid):
                if isBadVersion(mid - 1):  # 前面是true
                    return binarySearch(left, mid - 1)
                return mid
            else:
                return binarySearch(mid + 1, right)

        return binarySearch(1, n)


    """
    执行用时：32 ms, 在所有 Python3 提交中击败了81.44%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了50.22%的用户
    """
    # 我实现的官方题解
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left < right:
            mid = int(left + (right - left) / 2)
            if isBadVersion(mid):
                right = mid     # 答案在区间 [left, mid] 中
                # 常见错误 right = mid - 1
            else:
                left = mid + 1
        return left     # 此时 left == right


def isBadVersion(version):
    return True if version >= bad else False


# n = 5
# bad = 4
# n = 1
# bad = 1
# n = 10
# bad = 4
n = 3
bad = 2
s = Solution()
result = s.firstBadVersion(n)
print(result)
