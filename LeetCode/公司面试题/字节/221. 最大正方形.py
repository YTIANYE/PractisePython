"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'
"""

# 官方题解：二维动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare

# 我的题解：二维动态规划
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        length = 0
        m, n = len(matrix), len(matrix[0])
        dp = [
            [0] * n for _ in range(m)
        ]  # dp[i][j]表示以 i，j为正方形右下角格子的最大正方形边长

        def iscorrect(i, j, last_len):
            l = 1
            while l <= last_len:
                u = i - l
                left = j - l
                if matrix[u][j] == "0" or matrix[i][left] == "0":
                    break
                l += 1
            return l - 1

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
                    if i - 1 >= 0 and j - 1 >= 0:  # 注意边界
                        last_len = dp[i - 1][j - 1]
                        if last_len != 0:
                            dp[i][j] += iscorrect(i, j, last_len)

        for i in range(m):
            for j in range(n):
                length = max(length, dp[i][j])

        return length * length

        """
        ["0","0","1"],
        ["0","1","1"],
        ["1","1","1"]

        ["0","0","0","1"],
        ["1","1","0","1"],
        ["1","1","1","1"],
        ["0","1","1","1"],
        ["0","1","1","1"]

        ["0","0","0","1","0","1","1","1"],
        ["0","1","1","0","0","1","0","1"],
        ["1","0","1","1","1","1","0","1"],
        ["0","0","0","1","0","0","0","0"],
        ["0","0","1","0","0","0","1","0"],
        ["1","1","1","0","0","1","1","1"],
        ["1","0","0","1","1","0","0","1"],
        ["0","1","0","0","1","1","0","0"],
        ["1","0","0","1","0","0","0","0"]
        """
