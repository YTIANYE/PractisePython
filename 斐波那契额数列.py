"""
    以下代码使用递归实现斐波那契额数列
"""


def fb(n):
    if n <= 1:
        return n
    else:
        return (fb(n-1) + fb(n-2))

n = int(input("请输入个数："))

for i in range(n):
    print(fb(i),end=" ")

