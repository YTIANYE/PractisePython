"""
给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。

 

示例 1:

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
示例 2:

输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]
 

提示:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""

# 我的题解：单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        1 2 3 4 3

        1   [-1], 1入栈 
        3   [-1， 1] 3> 1， 1出栈，3入栈    结果【-1】
        4   [-1, 3] 4 > 3, 3出栈，4入栈 【-1】
        3   [-1, 4] 3< 4, 3入栈，结果【4】
        2   [-1, 4, 3] 2入栈，结果【3】
        1   [-1, 4, 3, 2]， 1入栈， 结果【2】
        3   [-1, 4, 3,  2, 1] 1 2 3出栈， 结果【4】

        第一个数入栈
        倒序依次遍历前面的数
        遇到更大的，先出栈，后入栈；
        遇到更小的直接入栈；
        栈顶为结果，栈空-1
        """
        n = len(nums)
        res = [-1] * n 
        stack = [nums[0]]
        for _ in range(2):
            for i in range(n-1, -1, -1):
                while stack and nums[i] >= stack[-1]:   # 注意>=
                    stack.pop(-1)
                if stack:
                    res[i] = stack[-1]
                stack.append(nums[i])
        return res 

# 官方题解：单调栈
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)
        
        return ret
