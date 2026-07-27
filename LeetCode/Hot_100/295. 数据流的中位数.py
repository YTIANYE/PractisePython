"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:

MedianFinder() 初始化 MedianFinder 对象。

void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

示例 1：

输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
提示:

-105 <= num <= 105
在调用 findMedian 之前，数据结构中至少有一个元素
最多 5 * 104 次调用 addNum 和 findMedian
"""

# 我的题解 同官方题解： 大顶堆+小顶堆
class MedianFinder:

    def __init__(self):
        self.minnums = []  # 大顶堆，# 注意每次minnums数值进出取负
        self.maxnums = []  # 小顶堆
        self.mid = 0
        self.tag = False  # True 奇数 False 偶数

    def addNum(self, num: int) -> None:
        if num > self.mid:
            heapq.heappush(self.maxnums, num)
        else:
            heapq.heappush(self.minnums, -num)  # 负号
        self.tag = not self.tag
        if len(self.maxnums) - len(self.minnums) >= 2:
            temp = heapq.heappop(self.maxnums)
            heapq.heappush(self.minnums, -temp)  # 负号
        elif len(self.minnums) - len(self.maxnums) >= 1:
            temp = -heapq.heappop(self.minnums)  # 负号
            heapq.heappush(self.maxnums, temp)
        if self.tag:
            self.mid = self.maxnums[0]
        else:
            self.mid = (-self.minnums[0] + self.maxnums[0]) / 2  # 负号
        # print(self.minnums, self.maxnums, self.mid, self.tag)

    def findMedian(self) -> float:
        return self.mid


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 官方题解：有序序列
from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right
        
        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2
