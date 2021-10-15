"""
统计一个数字在排序数组中出现的次数。
"""
from typing import List


class Solution:
    # 我的题解: 顺序遍历
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了44.59%的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了32.95%的用户
    """

    def search1(self, nums: List[int], target: int) -> int:
        count = 0
        for num in nums:
            if num == target:
                count += 1
        return count

    # 我的题解：二分查找
    def search(self, nums: List[int], target: int) -> int:
        self.count = 0

        def find(left, right):  # left, right 都是下标
            if left > right:
                return
            mid = int((left + right) / 2)
            if target > nums[mid]:
                find(mid + 1, right)
            elif target < nums[mid]:
                find(left, mid - 1)
            else:       # 相等时两边都看一下
                self.count += 1
                find(mid + 1, right)
                find(left, mid - 1)

        find(0, len(nums) - 1)
        return self.count


solu = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [5, 7, 7, 8, 8, 10]
# target = 6
print(solu.search(nums, target))
