"""
 归并排序（英语：Merge sort，或mergesort），是创建在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。

分治法:

    分割：递归地把当前序列平均分割成两半。
    集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。

"""


def merge(arr, left, mid, right):   # 左闭右闭

    n1 = mid - left + 1
    n2 = right - mid
    arr1 = [0] * n1
    arr2 = [0] * n2
    for i in range(0, n1):
        arr1[i] = arr[left + i]
    for j in range(0, n2):
        arr2[j] = arr[mid + 1 + j]

    i = j = 0
    k = left
    while i < n1 and j < n2:
        arr[k] = min(arr1[i], arr2[j])
        k += 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge1(arr, left, mid, right):

    """
    arr1 = arr2 = []
    这样的初始化是错误的，相当于arr1 和 arr2 指向同一处地址
    即，是同一变量

    正确的赋值方式：
    arr1 = []
    arr2 = []

    注意，list的赋值不同于普通变量（如：a = b = 10）,需要分开单独赋值
    """
    arr1 = []
    arr2 = []

    for k in range(left, mid + 1):
        """
        注意不要随便使用append()函数，特别是出现递归调用或者循环
        append()会不断的向局部变量list后面添加，有时候需要的是覆盖
        """
        # arr1[]初始化为空的列表，添加元素用append()函数，不要用错C++的方式
        arr1.append(arr[k])
    for k in range(mid + 1, right + 1):
        arr2.append(arr[k])

    # print("arr1 = ", arr1)
    # print("arr2 = ", arr2)
    # print("arr = ", arr)

    i = j = 0
    k = left
    # 这个循环是错误的 while k <= right:
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            j += 1
            k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
        # try:
        #     a = arr2[j]
        #     arr[k] = a
        #     print("a = ", a, "k = ", k, "len(arr2) = ", len(arr2), "j = ", j)
        # except:
        #     print("arr1 = ", arr1)
        #     print("arr2 = ", arr2)
        #     print("arr = ", arr)
        # finally:
        #     j += 1
        #     k += 1


def mergeSort(arr, left, right):    # 左闭右闭
    if left < right:
        mid = int((right + left) / 2)
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge1(arr, left, mid, right)


arr = [12, 11, 13, 5, 6, 7, 10, 8, 9]
mergeSort(arr, 0, len(arr)-1)   # 左闭右闭
print(arr)

