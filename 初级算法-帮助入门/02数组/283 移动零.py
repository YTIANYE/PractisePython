"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""
from typing import List


class Solution:
    # 我的题解
    # 利用 pop append 方法
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了61.41% 的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了11.65% 的用户
    """

    def moveZeroes1(self, nums: List[int]) -> None:
        i = 0
        l = len(nums)
        while i < l:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                l -= 1
            else:
                i += 1

    # 我的题解
    # 利用双指针
    """
    执行用时：32 ms, 在所有 Python3 提交中击败了97.82% 的用户
    内存消耗：15.2 MB, 在所有 Python3 提交中击败了90.68% 的用户
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        nums[i: j] 中的数均为0，由左向右移动，
        遇到一个0添加进来，越来越长，直至移到数组末端
        i j 对应的数互换实现nums[i: j] 的移动
        """

        i = 0  # 记录nums[i: j] 中为0的第一个数
        j = 1  # 记录nums[i: j] 后第一个不为0的数

        while len(nums) > j and i < len(nums):
            if nums[j] == 0:
                j += 1
            elif nums[i] != 0:
                i += 1
            else:
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    # 以下交换速度比上面的方法要慢
                    # 执行用时：44 ms, 在所有 Python3 提交中击败了61.41% 的用户
                    # 内存消耗：15.2 MB, 在所有 Python3 提交中击败了83.39% 的用户
                    # nums[i] = nums[j]
                    # nums[j] = 0
                j += 1


nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
# nums = [1,0]
# nums = [0, 0, 1]
# nums = [1]
# nums = [0, 1, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print()
print(nums)
