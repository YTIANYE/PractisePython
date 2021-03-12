"""
 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
步骤为：

    挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
    分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
    递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。
"""


def partition1(arr, low, high):  #   左闭右开
    temp = arr[low]
    j = low + 1
    #   大于的不动，小于的就交换    j总是记录着第一个大于temp的数，随时准备与i遇见的第一个小于temp的数进行交换
    for i in range(low+1, high):
        if arr[i] < temp:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j-1], arr[low] = arr[low], arr[j-1]
    return j-1


def partition2(arr, low, high):   #   左闭右开
    temp = arr[low]
    i = low + 1
    j = high-1
    #   左右两边同时进行，左小右大，不符合的相互交换
    while i < j:
        while arr[i] < temp and i < j:
            i += 1
        while arr[j] > temp and i < j:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if arr[j] > temp:
        j -= 1
    arr[low], arr[j] = arr[j], arr[low]
    return j


def partition3(arr, low, high):   #   左闭右开
    temp = arr[low]
    i = low
    j = high-1
    #   左右两边同时进行，左小右大，不符合的相互交换
    while i < j:
        while arr[j] > temp and i < j:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        while arr[i] < temp and i < j:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return j

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition3(arr, low, high)

        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 12, 9, 1, 5, 0, 15, 11, 14, 3, 4, 13, 6, 2]
n = len(arr)
quickSort(arr, 0, n )    #   左闭右开
print("排序后的数组:", arr)
