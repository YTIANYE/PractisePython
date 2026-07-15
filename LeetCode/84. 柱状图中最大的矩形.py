"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4
 

提示：

1 <= heights.length <=105
0 <= heights[i] <= 104
"""

# 我的题解 —— 单调栈
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        n = len(heights)
        left, right = [-1] * n, [n] * n 
        stack = []
        # 左边最小值
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:   # 注意大于等于
                stack.pop()
            if stack :              
                left[i] = stack[-1]     # 注意记录方式
            stack.append(i)
        stack = []
        # 右边界最小值
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack :
                right[i] = stack[-1]
            stack.append(i)
        # print(right, left)
        for i in range(n):
            res = max(res, heights[i] * (right[i] - left[i] -1))    # 注意宽度算法
        return res 
            

# # 官方题解
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         left, right = [0] * n, [n] * n

#         mono_stack = list()
#         for i in range(n):
#             while mono_stack and heights[mono_stack[-1]] >= heights[i]:
#                 right[mono_stack[-1]] = i
#                 mono_stack.pop()
#             left[i] = mono_stack[-1] if mono_stack else -1
#             mono_stack.append(i)
        
#         ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
#         return ans


        