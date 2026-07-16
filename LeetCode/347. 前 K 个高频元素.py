"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1：

输入：nums = [1,1,1,2,2,3], k = 2

输出：[1,2]

示例 2：

输入：nums = [1], k = 1

输出：[1]

示例 3：

输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

输出：[1,2]

 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
 

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""

# 我的题解  堆排序，所有元素建堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hash = collections.defaultdict(int)  # 注意写法
        for num in nums:
            hash[num] += 1
        # [值，出现频率]
        array = [[k, v] for k, v in hash.items()]  # 注意遍历方式
        self.buildHeap(array, len(array))
        # print(array)
        for i in range(k):
            res.append(array[0][0])
            j = len(array) - 1 - i  # 注意计算方式
            array[0], array[j] = array[j], array[0]
            self.maxHeap(array, 0, j)
        return res

    def buildHeap(self, array, heapsize):
        index = heapsize // 2 - 1
        for i in range(index, -1, -1):
            self.maxHeap(array, i, heapsize)    # 注意是 i
            # print(array)
            """
            1
            1       2
            1 3     3 2
            4 2 1
            """

    def maxHeap(self, array, index, heapsize):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < heapsize and array[left][1] > array[largest][1]:  # 注意比较largest
            largest = left
        if right < heapsize and array[right][1] > array[largest][1]:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            self.maxHeap(array, largest, heapsize)  # 注意下次遍历起点

# # 我实现的官方题解——固定大小的堆排序
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         hash = collections.defaultdict(int)  # 注意写法
#         for num in nums:
#             hash[num] += 1
#         # 建 小顶堆
#         heap = []
#         for key, val in hash.items():  # 注意hash的遍历方式
#             heapq.heappush(heap, (val, key))  # 注意heappush的使用方式
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         for i in range(k):
#             val, key = heapq.heappop(heap)
#             res.append(key)
#         return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        # print(counter)
        array = [[val, key] for key, val in counter.items()]  # v:频次， k:值
        n = len(array)

        def quickselect(left, right, need): # 注意need含义
            if left == right:   # 必须加此出口，否则单元素区间会无限递归导致 TLE
                res.append(array[left][1])
                return
            pivot_idx = random.randint(left, right)
            array[left], array[pivot_idx] = array[pivot_idx], array[left]
            temp = array[left][0]
            l, r = left - 1, right + 1
            while l < r:
                l += 1
                while array[l][0] < temp:
                    l += 1
                r -= 1
                while array[r][0] > temp:
                    r -= 1
                if l < r:
                    array[r], array[l] = array[l], array[r]
            # 划分后的区间[left, r][r+1, right]
            cnt = right - r
            if cnt >= need:    # 注意边界条件
                quickselect(r + 1, right, need)
            else:
                for i in range(r+1, right + 1):
                    res.append(array[i][1])
                quickselect(left, r, need-cnt)  # 注意边界

        quickselect(0, n - 1, k)
        return res