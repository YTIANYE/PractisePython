"""
1582. 二进制矩阵中的特殊位置
已解答
简单
相关标签
premium lock icon
相关企业
提示
给定一个 m x n 的二进制矩阵 mat，返回矩阵 mat 中特殊位置的数量。

如果位置 (i, j) 满足 mat[i][j] == 1 并且行 i 与列 j 中的所有其他元素都是 0（行和列的下标从 0 开始计数），那么它被称为 特殊 位置。

 

示例 1：


输入：mat = [[1,0,0],[0,0,1],[1,0,0]]
输出：1
解释：位置 (1, 2) 是一个特殊位置，因为 mat[1][2] == 1 且第 1 行和第 2 列的其他所有元素都是 0。
示例 2：


输入：mat = [[1,0,0],[0,1,0],[0,0,1]]
输出：3
解释：位置 (0, 0)，(1, 1) 和 (2, 2) 都是特殊位置。
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] 是 0 或 1。
"""
from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        sum_row = [0] * m 
        sum_col = [0]*n 
        for i in range(0,m ):
            for j in range (0, n):
                sum_row[i] += mat[i][j]
                sum_col[j] += mat[i][j]
        print(sum_row, sum_col)

        res = 0
        for i in range(0,m ):
            for j in range (0, n):
                if mat[i][j] == 1 and sum_row[i] == 1 and sum_col[j] == 1:
                    res += 1
        return res

    def numSpecial_2(self, mat: List[List[int]]) -> int:
        for i, row in enumerate(mat):
            cnt1 = sum(row) - (i == 0)
            if cnt1:
                for j, x in enumerate(row):
                    if x == 1:
                        mat[0][j] += cnt1
        return sum(x == 1 for x in mat[0])


if __name__ == "__main__":
    solution = Solution()
    mat = [[1,0,0],[0,0,1],[1,0,0]]
    print(solution.numSpecial(mat))


                        
                
