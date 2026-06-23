"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def add_hash(k):
            if k in hash:
                hash[k] += 1
            else:
                hash[k] = 1

        res = 0
        hash = {}  # 记录前缀和出现次数
        he = 0
        add_hash(0)
        for i, num in enumerate(nums):
            he += num
            if he - k in hash:  # 关键条件
                res += hash[he - k]  # 加上前缀和的次数
            add_hash(he)
        return res
