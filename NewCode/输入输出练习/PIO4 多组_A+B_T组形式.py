"""
描述
给定 
t
t 组测试数据。
每组数据有两个整数 
a
a 和 
b
b ，请你求出 
a
+
b
a+b 的值。
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
每行有两个整数 
a
 
(
 
1
≤
a
≤
1
0
9
 
)
a ( 1≤a≤10 
9
  ) 和 
b
 
(
 
1
≤
b
≤
1
0
9
 
)
b ( 1≤b≤10 
9
  ) 。
输出描述：
输出 
t
t 行，每行一个整数，代表 
a
+
b
a+b 的值。
示例1
输入：
3
1 2
114 514
2024 727
复制
输出：
3
628
2751
"""

import sys


def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        a = int(input[idx])
        b = int(input[idx + 1])
        print(a + b)
        idx += 2


if __name__ == "__main__":
    main()
