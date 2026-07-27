"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]
 

提示：

1 <= n <= 9
"""

# # 我的题解 DFS 回溯
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         res = []
#         queen = []
#         def has_queen(i, j):    # 判断是否冲突，相比官方题解时间复杂度O(n)可以降为O(1)
#             for q in queen:
#                 x, y = q[0], q[1]
#                 if j == y:
#                     return True
#                 if abs(i-x) == abs(j-y):
#                     return True
#             return False 

#         def dfs(i):
#             if i == n :
#                 ans = ['.' * n for _ in range(n)]
#                 for q in queen:
#                     x, y = q[0], q[1]
#                     ans[x] = '.' * y + 'Q' + '.' * (n - y - 1)
#                 res.append(ans)
#             for j in range(n):
#                 if has_queen(i, j):
#                     continue 
#                 queen.append([i, j])
#                 dfs(i+1)
#                 queen.pop()
        
#         dfs(0)
#         return res 
                
# # 官方题解
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         def generateBoard():
#             board = list()
#             for i in range(n):
#                 row[queens[i]] = "Q"
#                 board.append("".join(row))  # list转字符串方式，比我的方式更优
#                 row[queens[i]] = "."
#             return board

#         def backtrack(row: int):
#             if row == n:
#                 board = generateBoard()
#                 solutions.append(board)
#             else:
#                 for i in range(n):
#                     if i in columns or row - i in diagonal1 or row + i in diagonal2:
#                         continue
#                     queens[row] = i
#                     columns.add(i)
#                     diagonal1.add(row - i)
#                     diagonal2.add(row + i)
#                     backtrack(row + 1)
#                     columns.remove(i)
#                     diagonal1.remove(row - i)
#                     diagonal2.remove(row + i)
                    
#         solutions = list()
#         queens = [-1] * n
#         columns = set()
#         diagonal1 = set()
#         diagonal2 = set()
#         row = ["."] * n
#         backtrack(0)
#         return solutions

# 我实现的官方题解 回溯
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queen = []  # 按顺序记录每一行的列坐标
        lie = set()
        left = set()  # 左斜 x - y
        right = set()  # 右斜 x + y

        def make():
            r = []
            for i in range(n):
                s = "." * queen[i] + "Q" + "." * (n - 1 - queen[i])
                r.append(s)
            return r

        def dfs(i):
            if i == n:
                r = make()
                res.append(r)
            for j in range(n):
                if j in lie or i - j in left or i + j in right:  # 注意判断条件
                    continue
                queen.append(j)
                lie.add(j)
                left.add(i - j)
                right.add(i + j)
                dfs(i + 1)
                lie.remove(j)
                left.remove(i - j)
                right.remove(i + j)
                queen.pop()  # 注意pop

        dfs(0)
        return res
