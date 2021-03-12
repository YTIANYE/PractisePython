"""
二分搜索是一种在有序数组中查找某一特定元素的搜索算法。
搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。
"""


#   对已经排好序的数组，返回x相匹配值的索引

def binarySerch(arr, left, right, x):

    if right >= 1:
        mid = int(left + (right - left) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySerch(arr, mid + 1, right, x)
        else:
            return binarySerch(arr, left, mid - 1, x)
        pass
    else:
        return -1


arr = [1, 3, 6, 8, 10, 13, 20, 24, 27, 29, 30]
for x in arr:
    print(binarySerch(arr, 0, len(arr) - 1, x))
