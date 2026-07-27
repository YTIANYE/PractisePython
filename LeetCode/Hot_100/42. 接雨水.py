"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution_0:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0 
        res = 0 
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]: 
                # 注意判断条件 如果 height[left]<height[right]，
                # 则必有 leftMax<rightMax，
                # 下标 left 处能接的雨水量等于 leftMax−height[left]
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1  # 从右往左
        return res 


class Solution_1:
    def trap(self, height: List[int]) -> int:
        res = 0 
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n 
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        for i in range(0, n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res 

class Solution_2:
    def trap(self, height: List[int]) -> int:
        res = 0 
        n = len(height) 
        stack = []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()
                if not stack:
                    break 
                left = stack[-1]
                res += (i - 1 - left) * (min(height[i], height[left]) - height[top])
            stack.append(i) 
        return res 