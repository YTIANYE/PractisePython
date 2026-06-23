"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
 

提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

# 大根堆
import collections
import heapq


class Solution_0:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans

# 单调队列
class Solution_1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans

# 单调队列
class Solution_2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        que = deque()   # 队首最大，逐个减小，存储下标
        for i in range(k):
            # 不需要首字符判断
            # if i== 0：
            #     que.add(i)
            #     continue 
            while que and nums[que[-1]] <= nums[i]:   # 注意小于等于 # 注意que[-1]只是下标
                que.pop()   # 注意pop用法
            que.append(i)      # 注意append用法

        res.append(nums[que[0]])
        for j in range(k, n):
            i = j - k
            while que and nums[que[-1]] <= nums[j]:
                que.pop()
            que.append(j)           # 注意下标 i < j 
            while i >= que[0]:     # 注意大于等于 # 注意while条件
                que.popleft()   # 注意popleft()方法
            res.append(nums[que[0]])

class Solution_3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = []
        heapq.heapify(q) # 默认小顶堆，转负数存大顶堆;初始化需要传入数组
        for i in range(k):
            heapq.heappush(q, [-nums[i], i]) # 注意方法，heappush(q, x)，注意元素为负值和下标
        res.append(-q[0][0])    # 注意第一个值
        for j in range(k, n):
            i = j - k 
            heapq.heappush(q, [-nums[j], j])
            while i >= q[0][1]:     # 注意q是堆,由q取下标；注意大于等于
                heapq.heappop(q) # 注意方法为heappop(q)
            res.append(-q[0][0])
        
        return res 