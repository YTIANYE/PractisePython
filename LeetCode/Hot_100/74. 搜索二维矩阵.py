"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

# # 官方题解 两次 二分查找
# from typing import List
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         top, bot = 0, m - 1
#         # 二分：找最后一个首元素 <= target 的行
#         while top <= bot:
#             mid = (top + bot) // 2
#             if matrix[mid][0] == target:
#                 return True
#             elif matrix[mid][0] < target:
#                 top = mid + 1
#             else:
#                 bot = mid - 1
#         # bot 就是目标行；bot < 0 代表所有行首元素都大于 target
#         if bot < 0:
#             return False
#         row = bot
#         l, r = 0, n - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if matrix[row][mid] == target:
#                 return True
#             elif matrix[row][mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return False

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left)// 2
            x = mid // n    #注意整除
            y = mid % n 
            if matrix[x][y] < target:
                left = mid + 1 
            elif matrix[x][y] > target:
                right = mid - 1
            else:
                return True 
        return False 
