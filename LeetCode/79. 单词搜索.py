"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
示例 2：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
示例 3：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false
 

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
 

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
"""

# 我的题解 DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(count, x, y):
            if count == len(word):
                return True
            if not (0 <= x < m and 0 <= y < n):
                return False
            if board[x][y] != word[count] or board[x][y] == "#":
                return False
            count += 1
            t = board[x][y]
            board[x][y] = "#"
            res = (
                dfs(count, x + 1, y)
                or dfs(count, x - 1, y)
                or dfs(count, x, y + 1)
                or dfs(count, x, y - 1)
            )
            board[x][y] = t
            return res

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False

# # 官方题解
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         def check(i: int, j: int, k: int) -> bool:
#             if board[i][j] != word[k]:
#                 return False
#             if k == len(word) - 1:
#                 return True
            
#             visited.add((i, j))
#             result = False
#             for di, dj in directions:
#                 newi, newj = i + di, j + dj
#                 if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
#                     if (newi, newj) not in visited:
#                         if check(newi, newj, k + 1):
#                             result = True
#                             break
            
#             visited.remove((i, j))
#             return result

#         h, w = len(board), len(board[0])
#         visited = set()
#         for i in range(h):
#             for j in range(w):
#                 if check(i, j, 0):
#                     return True
        
#         return False

