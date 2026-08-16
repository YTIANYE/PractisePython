"""
给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。

网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。

返回机器人能够到达右下角的不同路径数量。

测试用例保证答案小于等于 2 * 109。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1

"""

# 我的题解：二维动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1   # 注意初始条件
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or obstacleGrid[i][j] == 1:
                    continue
                up = 0 if i - 1 < 0 else dp[i - 1][j]
                left = 0 if j - 1 < 0 else dp[i][j - 1]
                dp[i][j] = up + left
        return dp[-1][-1]

# 我的题解：一维动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n 
        dp[0] = 0 if obstacleGrid[0][0] else 1   # 注意初始条件
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0):
                    continue 
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0 
                    continue 
                up = 0 if i - 1 < 0 else dp[j]
                left = 0 if j - 1 < 0 else dp[j - 1]
                dp[j] = up + left
        return dp[-1]

# 官方题解：一维动态规划
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        f = [0] * m
        f[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    f[j] = 0
                elif j > 0 and obstacleGrid[i][j - 1] == 0:
                    f[j] += f[j - 1]
        return f[-1]
