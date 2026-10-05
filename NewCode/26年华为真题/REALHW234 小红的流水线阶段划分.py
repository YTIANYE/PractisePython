"""
描述
小红把按顺序排列的 
n
n 层模型恰好划分为 
p
p 个非空连续阶段。每段计算时间之和不得超过 
T
T；在第 
i
i 层后切分会产生通信开销 
c
o
m
m
i
comm 
i
​
 。求合法划分的最小总通信开销，不存在则输出 -1。
输入描述：
第一行输入 
n
,
p
,
T
n,p,T；第二行输入每层时间；第三行在 
n
>
1
n>1 时输入 
n
−
1
n−1 个通信开销。
保证 
1
≤
p
≤
n
≤
1000
1≤p≤n≤1000，
1
≤
T
≤
1
0
5
1≤T≤10 
5
 ，层时间在 
[
1
,
100
]
[1,100]，通信开销在 
[
1
,
10
]
[1,10]。
输出描述：
输出最小通信开销，无解输出 -1。
示例1
输入：
5 3 10
2 4 6 3 7
1 1 1 1
复制
输出：
2
复制
说明：
划分为 [2,4]、[6,3]、[7]。
示例2
输入：
4 2 7
3 5 4 2
1 2 3
复制
输出：
-1
复制
说明：
不存在两段均不超过 7 的划分。
"""
from collections import deque
import sys

n, p, T = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

if n > 1:
    costs = list(map(int, sys.stdin.readline().split()))
else:
    costs = []

# 前缀和 prefix[0]=0, prefix[1]=times[0], prefix[2]=times[0]+times[1] ...
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + times[i]

INF = float("inf")
# dp[t][k]：前k层恰好分成 t+1 段最小开销
dp = [[INF] * (n + 1) for _ in range(p)]

# ===== 初始化 t=0：恰好1段（不切任何刀）=====
for k in range(1, n + 1):
    if prefix[k] <= T:
        dp[0][k] = 0  # 没有切分，代价0

# t 从1到p-1：计算 t+1 段
for t in range(1, p):
    q = deque()  # 单调队列：保存候选m，维护 dp[t-1][m]+costs[m-1] 递增
    # k：前k层，范围至少 t+1层才能切成 t+1段
    for k in range(t + 1, n + 1):
        m = k - 1
        # m是候选分割点：前m层分成t段
        if dp[t - 1][m] != INF:
            val = dp[t - 1][m] + costs[m - 1]
            # 单调队列维护：队尾>=当前值，弹出，保持队列递增
            while q and dp[t - 1][q[-1]] + costs[q[-1] - 1] >= val:
                q.pop()
            q.append(m)

        # 窗口左边界收缩：prefix[k]-prefix[m] > T 的m全部踢出窗口（不满足时间约束）
        while q and prefix[k] - prefix[q[0]] > T:
            q.popleft()

        # 队首就是满足条件的最小代价m
        if q:
            best_m = q[0]
            dp[t][k] = min(dp[t][k], dp[t - 1][best_m] + costs[best_m - 1])

answer = dp[p - 1][n]
print(-1 if answer == INF else answer)
