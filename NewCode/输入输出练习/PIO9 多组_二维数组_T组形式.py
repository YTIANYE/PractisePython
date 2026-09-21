"""
描述
给定 
t
t 组询问，每次询问给出一个 
n
n 行 
m
m 列的二维正整数数组 
a
a ，第 
i
i 行第 
j
j 列元素的值为 
a
i
,
j
a 
i,j
​
  。
请你分别求出每个数组的元素之和。
输入描述：
第一行有一个整数 
t
 
(
 
1
≤
t
≤
1
0
5
 
)
t ( 1≤t≤10 
5
  ) 。
随后 
t
t 组数据。
每组的第一行有两个整数 
n
 
(
 
1
≤
n
≤
1
0
3
 
)
n ( 1≤n≤10 
3
  ) 和 
m
 
(
 
1
≤
m
≤
1
0
3
 
)
m ( 1≤m≤10 
3
  ) 。
每组的随后 
n
n 行，每行有 
m
m 个整数 
a
i
,
j
 
(
 
1
≤
a
i
,
j
≤
1
0
9
 
)
a 
i,j
​
  ( 1≤a 
i,j
​
 ≤10 
9
  ) 。
保证 
∑
n
⋅
m
≤
1
0
6
∑n⋅m≤10 
6
  。
输出描述：
输出 
t
t 行，每行一个整数，代表数组元素之和。
示例1
输入：
3
3 4
1 2 3 4
5 6 7 8
9 10 11 12
1 1
2024
3 2
1 1
4 5
1 4
复制
输出：
78
2024
16
复制
"""

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    total = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        total += sum(row)
    print(total)
