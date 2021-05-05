"""
测试  numpy
"""
import numpy as np


class test_numpy:

    # 求向量的距离公式
    def test_aquare(self):
        loc1 = np.zeros((1, 2))
        loc2 = np.zeros((1, 2))
        loc1[0] = [1, 2]
        loc2[0] = [4, 6]
        ins = np.sqrt(np.sum(np.square(loc1 - loc2)))
        print(ins)

    # 测试np.argwhere(), 找到n维数组中特定数值的索引
    def test_argwhere(self):
        x = np.array([1, -1, 1, -1])
        index = np.argwhere(x == 1)
        print(index)
        """
        [[0]
        [2]]
        """

    # 测试正态分布
    def test_normal(self):
        nums = [1, 2, 3, 4]
        n = np.random.normal(nums, 0.9)
        print(n)
        c = np.clip(n, 1, 3)
        print(c)


t = test_numpy()

t.test_normal()
