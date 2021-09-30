"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。


示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。
示例 2：

输入：x = 3, y = 1
输出：1


提示：

0 <=x, y <= 231 - 1

"""


class Solution:
    # 我的题解
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了70.51%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了26.79%的用户
    """

    def hammingDistance1(self, x: int, y: int) -> int:
        str_x = bin(x)[2:]  # 转化成二进制字符串，头两位会有“0b”
        str_y = bin(y)[2:]
        lenx = len(str_x)
        leny = len(str_y)
        length = abs(lenx - leny)
        if lenx < leny:
            str_x = '0' * length + str_x
        else:
            str_y = '0' * length + str_y

        count = 0
        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                count += 1
        return count

    # 我实现的官方题解
    # 移位实现位计数
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了42.39%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了83.03%的用户
    """

    def hammingDistance2(self, x: int, y: int) -> int:
        s = x ^ y
        count = 0
        while s:
            count += s & 1
            s >>= 1
        return count

    # 我实现的官方题解
    # Brian Kernighan 算法
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了42.39%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了68.64%的用户
    """
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        count = 0
        while s:
            s = s & (s - 1)
            count += 1
        return count


s = Solution()
x = 0
y = 0
print(s.hammingDistance(x, y))
