"""
    1.  关于列表的测试
"""


def testList():
    arr = [1, 2, 3, 4]
    arr1 = []
    testAppend(arr, arr1)
    testNulllist(arr1)


# 测试 append()函数
def testAppend(arr, arr1):
    for i in range(len(arr)):
        arr1.append(arr[i])


# 测试空列表的长度，为0
def testNulllist(arr1):
    print(arr1)
    print(len([]))


# 测试初始化数组
def testInitarr():
    arr = [1 * 8]   # [8]
    print(arr)
    arr2 = [1] * 8  # [1, 1, 1, 1, 1, 1, 1, 1]
    print(arr2)

# 测试 连续的list赋值 与 连续的变量赋值
def testListandInt():
    # 采用此方式对list类型赋值，相当于arr 和 arr1 指向同一地址，两个变量为同一个，
    # 应避免对list进行此类赋值方式
    arr = arr1 = []
    arr.append(1)
    # Int类型不是这样的
    a = b = 0
    print(arr, arr1)
    print(a, b)


"""
    2.  关于循环的测试
"""


# 测试for循环左闭右开的设定 在步长为-1时是否有效
def testFor():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(arr), -1, -1):   # 左闭右开，不会打印 -1
        # print(arr[i])   # 会报错 IndexError: list index out of range
        print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1 0
    print()

    # 测试数组初始化中包含 for 语句
    count = [0 for i in range(5)]
    print("count:", count)    # output: [0, 0, 0, 0, 0]
    ans = ["" for _ in arr]
    print("ans:", ans)      # ans: ['', '', '', '', '', '', '', '', '', '']



if __name__ == "__main__":
    # testList()
    # testListandInt()
    # testFor()
    testInitarr()
    pass


