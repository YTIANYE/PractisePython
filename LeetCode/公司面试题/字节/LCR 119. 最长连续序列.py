"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 104
-109 <= nums[i] <= 109
 

进阶：可以设计并实现时间复杂度为 O(n) 的解决方案吗？



"""

# 我实现的官方题解：集合、哈希
# 关键点：如果num-1在集合中，则跳过，因为num-1会被计算在内
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_l = 0 
        for num in s:
            if num - 1 in s:
                continue 
            i = num 
            l = 0 
            while i in s:
                i += 1
                l += 1
            max_l = max(max_l, l)
        return max_l
        

        
            
