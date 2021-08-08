"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""


class Solution:
    # 我的题解: 迭代
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了79.69%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.21%的用户
    """
    """
    n       方法
    (1)     1
    (2)     2
    (3)     3 = (2) + (1)
    (4)     5 = (3) + (2)
    (5)     8 = (4) + (3)
    (n)     (n-1) + (n-2)
    """

    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        sum = [0] * (n + 1)
        sum[1], sum[2] = 1, 2
        for i in range(3, n + 1):
            sum[i] = sum[i - 2] + sum[i - 1]
        return sum[n]

    """
    执行用时：32 ms, 在所有 Python3 提交中击败了79.69%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了15.86%的用户
    """

    def climbStairs2(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return third

    # 我实现的 官方题解 迭代
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了92.11%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.11%的用户
    """

    def climbStairs3(self, n: int) -> int:
        p = q = 0
        r = 1
        for i in range(1, n + 1):
            p = q
            q = r
            r = p + q
        return r

    # 我的题解： 递归
    """超出时间限制"""

    def climbStairs4(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 我实现的 官方题解 方法二：矩阵快速幂
    """    
    # 关于 f(x) = 2f(x-1) + 3f(x -2) + 4c 化成齐次线性递推
    # f(x) + c = 2[f(x-1) + c] + 3[f(x-2) + c]
    # g(x) = f(x) + c
    # g(x) = 2g(x-1) + 3g(x-2)
    # g(n+1)    2 3  n  g(1)
    # g(n)      1 0     g(0)
    """
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了92.11%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.32%的用户
    """

    def climbStairs5(self, n: int) -> int:

        # 矩阵相乘
        def matrix_nul(matrix1, matrix2):
            m = len(matrix1)        # 行数
            n = len(matrix2[0])
            matrix = [[] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    sum = 0
                    for k in range(len(matrix1[0])):
                        sum += matrix1[i][k] * matrix2[k][j]
                    matrix[i].append(sum)
            return matrix

        matrix = [
            [1, 1],
            [1, 0]
        ]
        matrix1 = [
            [1, 0],
            [0, 1]
        ]
        for i in range(n):      # 迭代n次，这里相当于 matrix 的 n-1 次方，而不是n次方，所以后面返回f[0][0] 而不是 f[0][1]
            matrix1 = matrix_nul(matrix, matrix1)
        f = matrix_nul(matrix1, [[1], [0]])
        return f[0][0]



s = Solution()
# n = 44  # 递归会慢很多
n = 44
print(s.climbStairs(n))


# 总结
"""
总结
这里形成的数列正好是斐波那契数列，答案要求的 f(n)f(n) 即是斐波那契数列的第 nn 项（下标从 00 开始）。我们来总结一下斐波那契数列第 nn 项的求解方法：

    1   n 比较小的时候，可以直接使用过递归法求解，不做任何记忆化操作，时间复杂度是 O(2^n)，存在很多冗余计算。
    2   一般情况下，我们使用「记忆化搜索」或者「迭代」的方法，实现这个转移方程，时间复杂度和空间复杂度都可以做到 O(n)。
    3   为了优化空间复杂度，我们可以不用保存f(x−2) 之前的项，我们只用三个变量来维护 f(x)、f(x−1) 和f(x−2)，
你可以理解成是把「滚动数组思想」应用在了动态规划中，也可以理解成是一种递推，这样把空间复杂度优化到了O(1)。
    4   随着 n 的不断增大O(n) 可能已经不能满足我们的需要了，我们可以用「矩阵快速幂」的方法把算法加速到O(logn)。
    5   我们也可以把 n 代入斐波那契数列的通项公式计算结果，但是如果我们用浮点数计算来实现，可能会产生精度误差。

"""
