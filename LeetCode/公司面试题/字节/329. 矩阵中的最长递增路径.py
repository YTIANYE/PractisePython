"""
给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。

 

示例 1：


输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。
示例 2：


输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
示例 3：

输入：matrix = [[1]]
输出：1
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""

# 官方题解 ：记忆化搜索 + 深度优先搜索
from functools import lru_cache
class Solution:
    
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            for dx, dy in Solution.DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans


# 官方题解 ：拓补排序 + BFS
class Solution:

    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        rows, columns = len(matrix), len(matrix[0])
        outdegrees = [[0] * columns for _ in range(rows)]
        queue = collections.deque()
        for i in range(rows):
            for j in range(columns):
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = i + dx, j + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[i][j]:
                        outdegrees[i][j] += 1
                if outdegrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            ans += 1
            size = len(queue)
            for _ in range(size):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    newRow, newColumn = row + dx, column + dy
                    if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] < matrix[row][column]:
                        outdegrees[newRow][newColumn] -= 1
                        if outdegrees[newRow][newColumn] == 0:
                            queue.append((newRow, newColumn))
        
        return ans


# 我的题解：记忆化搜索 + 深度优先搜索
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        self.tags = [[0] * n for _ in range(m)]
        self.res = 0

        def dfs(x, y, value):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0
            if matrix[x][y] <= value:  # 注意不能等于
                return 0
            if self.tags[x][y] != 0:
                return self.tags[x][y]

            self.tags[x][y] = (
                max(
                    dfs(x + 1, y, matrix[x][y]),
                    dfs(x - 1, y, matrix[x][y]),
                    dfs(x, y + 1, matrix[x][y]),
                    dfs(x, y - 1, matrix[x][y]),
                )
                + 1
            )
            self.res = max(self.res, self.tags[x][y])
            return self.tags[x][y]

        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        return self.res