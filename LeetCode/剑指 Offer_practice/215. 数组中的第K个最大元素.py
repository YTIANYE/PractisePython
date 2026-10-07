"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4


提示：
1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104

"""
import heapq
from typing import List

"""
执行用时：92 ms, 在所有 Python3 提交中击败了38.92%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了58.57%的用户
"""


class Solution:

    # 小根堆
    def findKthLargest1(self, nums: List[int], k: int) -> int:

        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            heap.append(num)
            heap.sort()
            heap.pop(0)

        # print(heap)
        return heap[0]

    # 大根堆
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heap[0]
