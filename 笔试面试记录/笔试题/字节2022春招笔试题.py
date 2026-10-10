# 3题
"""
魔法棒每一秒增加1个单位，同时魔法棒可以被分成两半，这两半具有以上性质
从0s开始，每隔1秒进行一次如下操作：（包括第0秒）
寻找当前长度为偶数的最长的魔法棒，分为相同的两半，没有符合要求的就不分
问：0秒时长度为x，n秒后，手中最长的魔法棒长度是多少？

0 <x < 10000000, 0<=n<=1000000

例子：
1 1
1
例子：
4 0
2
例子
1 6
4
"""

import heapq
import sys


# 方式一：通过33%
# 方式二：不清楚通过率


class Solution:

    def __init__(self, x):
        # self.hp = [x]
        # heapq.heapify(self.hp)  # 小顶堆
        if x % 2 == 0:
            self.nums = [[int(x / 2), 0], [int(x / 2), 0]]
        else:
            self.nums = [[x, 0]]
        self.time = 0

    def half1(self):
        nums = []
        while len(self.hp) != 0 and -self.hp[0] % 2 == 1:
            nums.append(heapq.heappop(self.hp))

        tag = False
        if len(self.hp) != 0:
            temp = heapq.heappop(self.hp)
            tag = True

        for num in nums:
            heapq.heappush(self.hp, num)
        for i in range(len(self.hp)):
            self.hp[i] -= 1

        if tag:
            heapq.heappush(self.hp, int(temp / 2))
            heapq.heappush(self.hp, int(temp / 2))

    def half(self):
        for i in range(len(self.nums)):
            num = self.nums[i]
            value = num[0] + self.time - num[1]
            if value % 2 == 0:
                self.nums = self.nums[:i] + self.nums[i + 1:]
                self.nums.append([int(value / 2), self.time])
                self.nums.append([int(value / 2), self.time])
                break



if __name__ == "__main__":
    line = input()
    a = line.split()
    x, n = int(a[0]), int(a[1])
    # solu = Solution(-x)
    solu = Solution(x)

    # for i in range(n+1):
    #     solu.half()
    for i in range(n):
        solu.half()
        solu.time += 1

    # print(-solu.hp[0])
    print(solu.nums[0][0] + solu.time - solu.nums[0][1])
