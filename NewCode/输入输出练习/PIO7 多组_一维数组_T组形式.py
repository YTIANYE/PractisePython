"""
描述
给定 
t
t 组询问，每次询问给出一个长度为 
n
n 的正整数数组 
a
a ，第 
i
i 个元素的值为 
a
i
a 
i
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
每组的第二行有 
n
n 个整数 
a
i
 
(
 
1
≤
a
i
≤
1
0
9
 
)
a 
i
​
  ( 1≤a 
i
​
 ≤10 
9
  ) 。
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
t 行，每行一个整数，代表数组元素之和。
示例1
输入：
3
3
1 4 7
1
1000
2
1 2
复制
输出：
12
1000
3
"""

import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    ptr = 0
    t = data[ptr]
    ptr += 1
    for _ in range(t):
        n = data[ptr]
        ptr += 1
        s = sum(data[ptr : ptr + n])
        ptr += n
        print(s)


if __name__ == "__main__":
    main()
