"""
给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0 ，则返回执行操作后 数组中连续 1 的最大个数 。

 

示例 1：

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
示例 2：

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1
0 <= k <= nums.length
"""
# 豆包题解 ： 滑动窗口
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_cnt = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            # 窗口内0超k，移动左边界收缩
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# 我的题解：滑动窗口
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        que = collections.deque([])  # 注意使用方式
        n = len(nums)
        res = 0
        left = -1   # 开头1前面的0的位置
        right = -1  # 末尾1的位置

        for i in range(n):
            if nums[i] == 0:
                if k == 0 : # 注意特殊情况
                    left = right  = i 
                    continue 
                if len(que) == k  :  # 注意k!= 0
                    j = que.popleft()
                    left = j
                que.append(i)
            right = i
            res = max(res, right - left)
            # print("i:", i, "left:", left, "right:", right, "res:", res )
        return res



# 官方题解：滑动窗口
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0
        
        for right in range(n):
            rsum += 1 - nums[right]
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
