"""
一个公司为每一个员工买衣服，有D,E,F三种衣服，每一种衣服给员工i的开心值分别为Di，Ei，Fi，
但是员工不愿意和他的直系boss衣服一样，求所有人开心值和的最大值

输入：
n，代表n个员工
n行，第i行 为Di，Ei，Fi
下面n-1行 每一行为 a b 代表a是b的直属boss

样例输入：
3
2 4 9
1 3 5
1 2 3
0 1
0 2
样例输出：
14

0号选F，1号选E,2号选E，9+3+2=14
"""
from typing import List


class Solution:

    # 暴力遍历每一种情况，index长度为n,每个值（0,1,2）对应员工所选的衣服，三进制的方式
    def increase(self, index: List[int]):
        index[0] += 1
        for i in range(0, len(index) - 1):
            if index[i] == 3:
                index[i] = 0
                index[i + 1] += 1
        return index

    def maxHappy(self, n: int, arr: List[List[int]], boss: List[List[int]]):
        max = 0
        memory = []  # 存放开心值
        index = [0] * n  # index存放 0 1 2 ，n个值对应n个员工选的衣服
        for i in range(0, 3 ** n):      # 一共有3**n种情况
            for j in range(0, n):
                memory.append(arr[j][index[j]])
            if self.isNotBoss(index, boss):     # 不存在直属领导和员工衣服一样的情况
                if max < sum(memory):
                    max = sum(memory)
            index = self.increase(index)        # 下一种情况
            memory = []
        return max

    # 判断当前序列中是否包含直属领导和员工衣服一样的情况，不存在则返回True
    def isNotBoss(self, index: List[int], boss: List[List[int]]) -> bool:
        for i in range(0, len(boss)):
            if index[boss[i][0]] == index[boss[i][1]]:
                return False
        return True


s = Solution()
n = 3
arr = [[2, 4, 9],
       [1, 3, 5],
       [1, 2, 3]]
boss = [[0, 1],
        [0, 2]]
"""
n = 4
arr = [[2, 4, 9],
       [1, 3, 5],
       [1, 2, 3],
       [5, 7, 1]]
boss = [[0, 1],
        [0, 2]]
"""
print(s.maxHappy(n, arr, boss))
