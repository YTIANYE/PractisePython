"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4]的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
示例 2：

输入：
["MedianFinder","addNum","findMedian","addNum","findMedian"]
[[],[2],[],[3],[]]
输出：[null,null,2.00000,null,2.50000]

限制：

最多会对 addNum、findMedian 进行 50000 次调用。


"""


# 我实现的官方题解：堆排序
from heapq import heappush, heappop

"""
执行用时：168 ms, 在所有 Python3 提交中击败了67.44%的用户内存消耗：26 MB, 在所有 Python3 提交中击败了5.04%的用户
"""

class MedianFinder:

    def __init__(self):
        self.A = []  # 小顶堆，保存较大的一半
        self.B = []  # 大顶堆，保存较小的一半   # 存取要加负号

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B):
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))
        else:
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))

    def findMedian(self) -> float:
        if len(self.B) == len(self.A):
            return (-self.B[0] + self.A[0]) / 2.0
        else:
            return self.A[0]
