"""
描述
给定 
t
t 组询问，每次给出一个长度为 
n
n 的带空格的字符串 
s
s ，请你去掉空格之后，将其倒置，然后输出。
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
s，仅包含小写英文字符和空格，保证字符串首尾都不是空格。
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
9
one space
11
two  spaces
14
three   spaces
复制
输出：
ecapseno
secapsowt
secapseerht
复制
"""





import sys

t = int(input())

for line in sys.stdin:
    n = int(line)
    s = input().split()
    new_s = "".join(s)
    print(new_s[::-1])


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    res = ""
    for i in range(n-1, -1, -1):
        if s[i] != " ":
            res += s[i] 
    print(res)

