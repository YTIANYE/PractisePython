"""
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。



示例 1:

输入: [1,2,3,1]
输出: true

示例 2:

输入: [1,2,3,4]
输出: false

"""
from typing import List


class Solution:
    """
    执行用时：76 ms, 在所有 Python3 提交中击败了6.43% 的用户
    内存消耗：19.8 MB, 在所有 Python3 提交中击败了84.99% 的用户
    """
    def containsDuplicate1(self, nums: List[int]) -> bool:
        new_set = set()
        for i in range(len(nums)):
            if nums[i] in new_set:
                return True
            else:
                new_set.add(nums[i])
        return False
    pass

    """
    执行用时：64 ms, 在所有 Python3 提交中击败了6.43% 的用户
    内存消耗：20.2 MB, 在所有 Python3 提交中击败了35.00% 的用户
    """

    def containsDuplicate2(self, nums: List[int]) -> bool:
        new_set = set(nums)
        if len(nums) == len(new_set):
            return False
        else:
            return True

    """
    执行用时：48 ms, 在所有 Python3 提交中击败了55.50% 的用户
    内存消耗：20.2 MB, 在所有 Python3 提交中击败了44.21% 的用户
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

li = [1,1,1,3,3,4,3,2,4,2]
# li = [1,2,3,4]
s = Solution()
print(s.containsDuplicate(li))


