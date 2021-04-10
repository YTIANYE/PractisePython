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
    arr = [1 * 8]  # [8]
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


# 测试 sorted 函数和 list.sort()
def testsorted():
    nums = [1, 0, 1]
    sorted(nums)    # 不改变原列表
    print(nums)     # [1, 0, 1]
    print(sorted(nums)) # 返回新列表 [0, 1, 1]
    nums.sort()     # 改变原列表
    print(nums)     # [0, 1, 1]


if __name__ == "__main__":

    testsorted()    # 由小到大排序
    pass
