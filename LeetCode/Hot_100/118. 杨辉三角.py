"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。



 

示例 1:

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
示例 2:

输入: numRows = 1
输出: [[1]]
 

提示:

1 <= numRows <= 30

"""

# 我的题解 动态规划
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            templist = [1] * i 
            if i > 2:
                for j in range(1, i-1):
                    templist[j] = res[-1][j] + res[-1][j-1]
            res.append(templist)
        return res 
        
