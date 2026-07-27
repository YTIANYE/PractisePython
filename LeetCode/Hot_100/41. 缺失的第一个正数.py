"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

示例 1：

输入：nums = [1,2,0]
输出：3
解释：范围 [1,2] 中的数字都在数组中。
示例 2：

输入：nums = [3,4,-1,1]
输出：2
解释：1 在数组中，但 2 没有。
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
解释：最小的正数 1 没有出现。
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""

# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         jihe = set(nums)
#         i = 1
#         while True:
#             if i not in jihe:
#                 return i
#             i += 1


class Solution_1:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])  # 绝对值
            if num <= n:  # 小于等于
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:  # 大于符号
                return i + 1
        return n + 1
    
class Solution_2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:    # 注意是while循环
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                """
                nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                核心原因：Python 赋值时「先算右侧所有值，再从左到右赋值左侧」，原顺序会导致 nums[i] 提前被修改，进而让目标索引计算错误；
                关键优化：交换顺序改为「先赋值目标索引（nums[nums[i]-1]），再赋值当前索引（nums[i]）」，确保索引计算始终基于原始值；
                最终效果：避免死循环 / 无效计算，解决超时问题，同时保持逻辑正确性。
                """
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1




