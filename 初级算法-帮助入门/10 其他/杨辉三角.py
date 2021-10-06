"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:

输入: numRows = 5
输出:  0   [[1],
      1   [1,1],
      2   [1,2,1],
      3   [1,3,3,1],
      4   [1,4,6,4,1]]
           0 1 2 3 4
示例2:

输入: numRows = 1
输出: [[1]]

1 <= numRows <= 30
"""
from typing import List


class Solution:
    # 我的题解
    """
    执行用时：24 ms, 在所有 Python3 提交中击败了96.50%的用户
    内存消耗：14.7 MB, 在所有 Python3 提交中击败了98.02%的用户
    """
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    num = 1
                else:
                    num = result[-1][j-1] + result[-1][j]
                row.append(num)
            result.append(row)
        return result


s = Solution()
numRows = 5
print(s.generate(numRows))