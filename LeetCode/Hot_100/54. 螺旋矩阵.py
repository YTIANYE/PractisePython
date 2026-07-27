"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        0,0
        0,3
        2,3
        2,0
        1,0
        1,2
        right, down, left, up
        """
        # ends = [] 
        # right, down, left, up
        # up_end++, right_end--, down_end--, left_end++
        # [-1, 4, 3, -1]
        # right [0, 4, 3, -1]
        # down  [0, 3, 3, -1]
        # left  [0, 3, 2, -1]
        # up    [0, 3, 2, 0]
        # right [1, 3, 2, 0]
        # down 
        m, n = len(matrix), len(matrix[0])
        res = []
        ends = [-1, n, m, -1]
        fx = 0
        x, y = 0, 0
        while True:
            if fx == 0 or fx == 2:
                if ends[1] - ends[3] == 1:  # 右边界 - 左边界
                    break
            else: # if fx == 1 or fx == 3:
                if ends[2] - ends[0] == 1:
                    break 

            if fx == 0:
                while y < ends[1]:
                    print(x, y)
                    res.append(matrix[x][y])
                    y += 1
                ends[0] += 1
                y -= 1
                x += 1
            elif fx == 1:
                while x < ends[2]:
                    print(x, y)
                    res.append(matrix[x][y])
                    x += 1
                ends[1] -= 1
                x -= 1
                y -= 1
            elif fx == 2:
                while y > ends[3]:
                    print(x, y)
                    res.append(matrix[x][y])
                    y -= 1
                ends[2] -= 1
                y += 1
                x -= 1
            else: # fx == 3:
                while x > ends[0]:
                    print(x, y)
                    res.append(matrix[x][y])
                    x -= 1
                ends[3] += 1
                x += 1
                y += 1
            print(x, y, res)
            # 下一步
            fx = (fx + 1) % 4
        return res 
    

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list()
        
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/spiral-matrix/solutions/275393/luo-xuan-ju-zhen-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。