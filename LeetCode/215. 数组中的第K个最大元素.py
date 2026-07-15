"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

# # 我实现的官方题解——快速选择
# import random
# from typing import List
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         target = n - k 
#         def quickselect(left, right):
#             if left == right:
#                 return nums[target]
#             rd = random.randint(left, right)
#             nums[left], nums[rd] = nums[rd], nums[left]
#             pivot = nums[left]  # 注意值下标
#             i = left - 1
#             j = right + 1
#             while i < j:
#                 i += 1
#                 while nums[i] < pivot:
#                     i += 1
#                 j -= 1
#                 while nums[j] > pivot:
#                     j -= 1
#                 if i < j:       # 注意条件
#                     nums[i], nums[j] = nums[j], nums[i]
#             # 不需要交换pivot！区间规则 [left,j] <= pivot
#             if target <= j:     # 注意一定j
#                 return quickselect(left, j)
#             else:
#                 return quickselect(j + 1, right)
#         return quickselect(0, n - 1)
    

# 我实现的官方题解——堆排序
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.buildMaxHeap(nums, n)
        for i in range(k - 1):  # 注意次数k-1
            j = n - 1 - i   # 注意j的计算
            nums[j], nums[0] = nums[0], nums[j]
            self.maxHeapify(nums, 0, j)
        return nums[0]

    def buildMaxHeap(self, nums, heapSize):
        # 0,
        # 1, 2,
        # 3, 4, 5, 6
        # left = root * 2 + 1
        # right = root * 2 + 2
        root = (heapSize - 1 - 1) // 2
        for i in range(root, -1, -1):
            self.maxHeapify(nums, i, heapSize)

    def maxHeapify(self, nums, i, heapSize):
        l, r, largest = i * 2 + 1, i * 2 + 2, i
        if l < heapSize and nums[l] > nums[largest]:    # 注意比较条件
            largest = l
        if r < heapSize and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.maxHeapify(nums, largest, heapSize)
