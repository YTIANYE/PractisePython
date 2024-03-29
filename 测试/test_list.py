"""
    1.  关于列表的测试
"""
import numpy as np


# 测试 append 和 空列表长度
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
    arr3 = [[0] * 3] * 3
    print(arr3)     # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    arr4 = [[]] * 3
    print(arr4)     # [[], [], []]
    arr4[0].append(1)
    print(arr4)     # [[1], [1], [1]]


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


# 测试 npzero
def testnpzero():
    cal = np.zeros((1, 2))  # [[0. 0.]] 一维2列
    print(cal)


# 测试复制数组
def testcopy():
    nums = [1, 2, 3]
    nums1 = list(nums)              # 复制nums的内容生成一个新的list
    nums2 = [num for num in nums]   # 复制nums的内容生成一个新的list
    nums3 = nums                    # nums3和nums 是同一引用
    print(nums, nums1, nums2, nums3)
    nums1.pop()
    nums2.pop()
    print(nums)
    nums3.pop()
    print(nums)


if __name__ == "__main__":

    testcopy()
    pass
