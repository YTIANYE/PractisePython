"""
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。
"""


def heapify(arr, n, i):   # n 数组长度，结点个数     i 当前结点
    largest = i     # 当前节点
    left = i * 2 + 1
    right = left + 1    # 右节点

    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        # 经过修正之前的错误代码 heapify(arr, n, i - 1)
        heapify(arr, n, largest)    # 当有一个相对较小的数被从上面换下来，需继续向下进行比较

def heapSort(arr):

    n = len(arr)

    for i in range(n - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        # 经过修正之前的错误代码 heapify(arr, n, i)
        heapify(arr, i, 0)  # 排序好最大的结点，需对顶部结点进行调整


arr = [3, 6, 2, 5, 1, 4]
heapSort(arr)
print(arr)


"""


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n - 1, -1, -1):  # for i in range(n, -1, -1):
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("排序后")
for i in range(n):
    print("%d" % arr[i]),


"""
