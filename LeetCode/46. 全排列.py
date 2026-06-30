"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
 

"""

# 我实现的官方题解

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def insert(first):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):   # 起始是 first+1，跳过了自己和自己交换，会丢失大量排列！
                nums[first], nums[i] = nums[i], nums[first]
                insert(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        insert(0)
        return res
