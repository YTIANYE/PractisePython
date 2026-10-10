"""
描述
给定目标字符串 
T
T 和源字符串 
S
S。小红只能在 
S
S 的任意位置插入字符，求最少插入多少个字符，才能使 
T
T 成为新字符串的子序列。插入字符必须来自 
T
T 的字符集合。
输入描述：
第一行输入 
T
T，第二行输入 
S
S。保证二者只含小写字母，长度均在 
[
1
,
2500
]
[1,2500]。
输出描述：
输出最少插入字符数。
示例1
输入：
abc
ac
复制
输出：
1
复制
说明：
插入 b 即可。
示例2
输入：
abc
xyz
复制
输出：
3
复制
说明：
源串无法匹配目标串中的任何字符。
示例3
输入：
aaab
ab
复制
输出：
2
复制
说明：
还需插入两个 a。
"""

import sys

# 官方题解：一维DP
def main():
    p = sys.stdin.read().split()
    T, S = p[0], p[1]
    nT = len(T)
    if len(T) < len(S):
        T, S = S, T
    dp = [0] * (len(S) + 1)
    for x in T:
        prev = 0
        for j, y in enumerate(S, 1):
            curr = dp[j]
            dp[j] = prev + 1 if x == y else max(dp[j], dp[j - 1])
            prev = curr
    ans = nT - dp[len(S)]
    print(ans)


main()


# 我的题解：二维DP + 最大公共子序列
# 最少插入数量 = 目标串 T 的总长度 − T 和 S 的最长公共子序列 (LCS) 长度
def solve():
    T = input()  # 目标字符串
    S = input()  # 源字符串
    # print(T, S)
    n, m = len(T), len(S)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:  # 注意字符串坐标
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(n - dp[-1][-1])  # 注意返回值


solve()

