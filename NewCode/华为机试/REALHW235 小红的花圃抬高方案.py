"""
描述
小红要用土把所有花圃的最低高度尽量抬高。每单位土的填埋成本为 
U
U；每车最多运 
C
C 单位土，每启用一车另付运输费 
F
F，一车土可分给多个花圃。预算为 
B
B。求预算内所有花圃最终最低高度的最大值。
输入描述：
依次输入预算 
B
B、每车容量 
C
C、运输费 
F
F、单位填埋费 
U
U、花圃数 
n
n，最后输入 
n
n 个初始高度。
保证 
1
≤
B
≤
1
0
11
1≤B≤10 
11
 ，
1
≤
C
,
F
,
U
≤
100
1≤C,F,U≤100，
1
≤
n
≤
1
0
5
1≤n≤10 
5
 ，高度在 
[
0
,
1
0
6
]
[0,10 
6
 ]。
输出描述：
输出可达到的最大最低高度。
示例1
输入：
100
10
5
2
5
1 2 5 3 4
复制
输出：
11
复制
说明：
抬高到 11 需要 40 单位土，填埋费 80、运输费 20。
示例2
输入：
50
10
10
1
10
1 2 5 3 4 5 4 1 1 1
复制
输出：
4
复制
说明：
抬高到 4 总成本 35，抬高到 5 总成本 53。
"""

# 我的题解：

b = int(input())
c = int(input())
f = int(input())
u = int(input())
n = int(input())
h = list(map(int, input().split()))
# print(b, c, f, u, n, h)

price = c * u + f   # 满载车成本
count = b // price  # 满载车次数
less = b - count * price    # 剩余金额
less_c = 0 
if less > f:
    less_c = (less - f) // u
num = count * c + less_c    # 总共单位的土
# print(num)
# 由低到高，判断是否可以填平
h.sort()
total = 0
i = 0 
while i < n:
    total += h[i]
    if (i + 1) * h[i] - total > num :
        total -= h[i]
        break 
    i += 1
res = (num + total ) // i
print(res)



