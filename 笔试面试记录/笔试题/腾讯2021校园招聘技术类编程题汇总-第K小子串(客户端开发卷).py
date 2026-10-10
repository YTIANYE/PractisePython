"""
输入一个字符串 s，s 由小写英文字母组成，保证 s 长度小于等于 5000 并且大于等于 1。在 s 的所有不同的子串中，输出字典序第 k 小的字符串。
字符串中任意个连续的字符组成的子序列称为该字符串的子串。
字母序表示英文单词在字典中的先后顺序，即先比较第一个字母，若第一个字母相同，则比较第二个字母的字典序，依次类推，则可比较出该字符串的字典序大小。

数据范围：  ，
进阶：空间复杂度  ， 时间复杂度

输入描述:
第一行输出一个字符串 s，保证 s 长度小于等于 5000 大于等于 1。
第二行一个整数 k (1<= k <= 5)，保证 s 不同子串个数大于等于 k。

输出描述:
输出一个字符串表示答案。
输入例子1:
aabb
3
输出例子1:
aab
例子说明1:
不同的子串依次为：
a aa aab aabb ab abb b bb
所以答案为aab
输入例子2:
aaa
3
输出例子2:
aaa

"""
import heapq
import string
import sys


class Solution:

    def kthString(self, s: string, k: int):

        l = len(s)
        if l < 2:
            return s

        strs = []

        for i in range(l - 1):
            for j in range(i + 1, l + 1):
                if s[i:j] in strs:
                    continue

                elif len(strs) < k:
                    strs.append(s[i:j])
                    strs.sort()
                else:
                    if s[i:j] < strs[-1]:
                        strs.append(s[i:j])
                        strs.sort()
                        strs = strs[:-1]
                    else:  # 这里的加不进去，更长的肯定加不进去
                        break

        return strs[k - 1]


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    # print(s)
    k = int(sys.stdin.readline().strip())
    # print(k)

    solu = Solution()

    print(solu.kthString(s, k))
