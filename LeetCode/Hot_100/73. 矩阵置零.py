"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

 

示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

提示：

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        list1 = [1] * m 
        list2 = [1] * n 
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    list1[i] = 0 
                    list2[j] = 0 
        print(list1, list2)
        for i in range(m):
            if list1[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0 
        for j in range(n):
            if list2[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m, n = len(matrix), len(matrix[0])
#         row, col = [False] * m, [False] * n

#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row[i] = col[j] = True
        
#         for i in range(m):
#             for j in range(n):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/set-matrix-zeroes/solutions/669901/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution_1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # 行数
        n = len(matrix[0]) # 列数
        # 以矩阵第一行、第一列代替标记数组
        # 第一行标记哪一列是0，第一列标记哪一行是0
        hang = 1
        lie = 1 
        for i in range(m):
            if matrix[i][0] == 0:
                lie = 0 
                break 
        for j in range(n):
            if matrix[0][j] == 0:
                hang = 0
                break
        # 统计非首行首列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 处理非首行首列
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # 处理首行和首列
        if hang == 0:
            matrix[0] = [0] * n 
        if lie == 0:
            for i in range(m):
                matrix[i][0] = 0 
        
# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m, n = len(matrix), len(matrix[0])
#         flag_col0 = any(matrix[i][0] == 0 for i in range(m))
#         flag_row0 = any(matrix[0][j] == 0 for j in range(n))
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
        
#         if flag_col0:
#             for i in range(m):
#                 matrix[i][0] = 0
        
#         if flag_row0:
#             for j in range(n):
#                 matrix[0][j] = 0

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/set-matrix-zeroes/solutions/669901/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m, n = len(matrix), len(matrix[0])
#         flag_col0 = False
        
#         for i in range(m):
#             if matrix[i][0] == 0:
#                 flag_col0 = True
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
        
#         for i in range(m - 1, -1, -1):
#             for j in range(1, n):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
#             if flag_col0:
#                 matrix[i][0] = 0

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/set-matrix-zeroes/solutions/669901/ju-zhen-zhi-ling-by-leetcode-solution-9ll7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。