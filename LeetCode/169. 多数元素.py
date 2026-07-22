"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
 

提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
输入保证数组中一定有一个多数元素。
 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
"""

# 官方题解——摩尔投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if res == 0:
                res = num
            elif res == num:
                res += 1
            else:
                res -= 1
        return res

# 我的题解
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')
        count = 0 
        for num in nums:
            if num == res :
                count += 1
            else:
                if count == 0 :
                    res = num 
                    count += 1
                else:
                    count -= 1
        return res 
            
        