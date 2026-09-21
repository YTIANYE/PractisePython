"""
描述
给定一个 
n
n 行 
m
m 列的二维字符数组 
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
请你对行和列都倒置，然后输出之。
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
随后 
n
n 行，每行有 
m
m 个字符，仅包含小写英文字符 。
输出描述：
输出一个二维字符数组。
示例1
输入：
3 4
abcd
efgh
ijkl
复制
输出：
lkji
hgfe
dcba
复制
"""

n, m = map(int, input().split())
str = [""] * n 
for i in range(n):
    s = input()
    str[i] = s[::-1]
for i in range(n):
    print(str[n-1-i])