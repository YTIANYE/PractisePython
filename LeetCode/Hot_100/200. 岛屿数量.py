"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
示例 2：

输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""

# 我的题解
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        flags = [
            [False for i in range(n)] for j in range(m)
        ]  # 记录是否查看过,注意m 行 n 列
        count = 0

        def add_node(i, j):
            # print(flags)
            if grid[i][j] == "1" and flags[i][j] == False:  # 注意条件
                flags[i][j] = True
                if i - 1 >= 0:  # 注意边界
                    add_node(i - 1, j)
                if i + 1 < m:
                    add_node(i + 1, j)
                if j - 1 >= 0:  # 注意边界
                    add_node(i, j - 1)
                if j + 1 < n:
                    add_node(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and flags[i][j] == False:
                    count += 1
                    add_node(i, j)
        return count
