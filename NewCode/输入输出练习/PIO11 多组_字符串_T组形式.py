"""
描述
给定 
t
t 组询问，每次给出一个长度为 
n
n 的字符串 
s
s ，请你将其倒置，然后输出。
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
每组的第一行有一个整数 
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
  ) 。
每组的第二行有一个字符串 
s
s，仅包含小写英文字符。
保证 
∑
n
≤
1
0
5
∑n≤10 
5
  。
输出描述：
输出 
t
t 行，每行一个字符串，代表倒置后的字符串 
s
s 。
示例1
输入：
3
5
abcde
8
redocwon
9
tfarcenim
复制
输出：
edcba
nowcoder
minecraft
复制
"""


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(s[::-1])