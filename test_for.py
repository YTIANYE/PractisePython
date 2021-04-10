"""
    2.  关于循环的测试
"""


# 测试for循环左闭右开的设定 在步长为-1时是否有效
def testFor():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(arr), -1, -1):  # 左闭右开，不会打印 -1
        # print(arr[i])   # 会报错 IndexError: list index out of range
        print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1 0
    print()

    # 测试数组初始化中包含 for 语句
    count = [0 for i in range(5)]
    print("count:", count)  # output: [0, 0, 0, 0, 0]
    ans = ["" for _ in arr]
    print("ans:", ans)  # ans: ['', '', '', '', '', '', '', '', '', '']


# 测试反向循环访问时的区间
def testListSquare():
    # 反向循环的时候，注意第一个第二个参数与正向循环位置不同
    for i in range(5, 0, -1):   # 左闭右开
        print(i)


if __name__ == "__main__":
    # testList()
    # testListandInt()
    # testFor()
    # testInitarr()
    pass