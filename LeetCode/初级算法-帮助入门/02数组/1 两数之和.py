"""
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。


示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    只会存在一个有效答案
"""
from typing import List


class Solution:

    # 我的题解
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了66.61% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了13.46% 的用户
    """
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = target - nums[i]
            for j in range(i + 1, len(nums)):
                if num == nums[j]:
                    return [i, j]

    # 别人的题解 哈希表     明显提高内存
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了66.61% 的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了43.92% 的用户
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}    # key 数字  value nums的index
        for i in range(len(nums)):
            if target - nums[i] in dit:     # 判断键值是否在字典中的方式
                return [i, dit[target - nums[i]]]
            else:
                dit[nums[i]] = i




s = Solution()
nums = [2, 7, 11, 15]
target = 9
print(s.twoSum(nums, target))
