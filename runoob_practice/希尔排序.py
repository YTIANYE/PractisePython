"""
 希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。
"""


def shellSort(arr):
    n = len(arr)
    gap = int(n/2)

    while gap > 0:

        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 注意 >=
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            # 不是 arr[i] = temp
            arr[j] = temp

        # 不是 gap /= 2
        gap = int(gap/2)


arr = [5, 7, 2, 9, 0, 3]
shellSort(arr)
print(arr)