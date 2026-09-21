"""
描述
给定两个整数 
n
n 和 
m
m ，请你构造一个长度为 
n
n 的正整数数组，使得其元素之和为 
m
m 。
保证有 
n
≤
m
n≤m 。
输入描述：
第一行有两个整数 
n
 
(
 
1
≤
n
≤
1
0
5
 
)
n ( 1≤n≤10 
5
  ) 和 
m
 
(
 
n
≤
m
≤
1
0
9
 
)
m ( n≤m≤10 
9
  ) 。
输出描述：
输出 
n
n 个正整数，它们的和需要为 
m
m 。
示例1
输入：
3 6
复制
输出：
1 2 3
复制
"""


n, m = map(int, input().split())
for _ in range(n-1):
    print(1,end=" ")
print(m-(n-1))