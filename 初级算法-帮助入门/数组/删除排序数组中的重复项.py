"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 

提示：

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列

"""
from typing import List


class Solution:
    # 用时最少，内存最多
    # 使用 列表转集合 的方法
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了90.47%的用户
    内存消耗：16 MB, 在所有 Python3 提交中击败了5.05%的用户
    """

    def removeDuplicates(self, nums: List[int]) -> int:

        set_nums = set(nums)
        # 注意列表函数的使用，不能简单使用 = 更改列表内容
        nums.clear()
        # 不符合原地修改条件
        nums.extend(sorted(list(set_nums)))  # 结果要进行排序
        return len(set_nums)

    # 用时最长
    # 从后不断向前赋复制，遍历列表的暴力方法
    """
    执行用时：4296 ms, 在所有 Python3 提交中击败了5.00%的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了22.02%的用户
    """

    def movestep(self, nums: List[int], left, right, step):
        for i in range(left, right - step):
            nums[i] = nums[i + step]
        while step:
            nums.pop()
            step -= 1

    def removeDuplicates2(self, nums: List[int]) -> int:

        step = 0
        for i in range(len(nums) - 1, 0, -1):  # 注意第二个参数是 0 ，不是 -1
            if nums[i] == nums[i - 1]:
                step += 1
            else:
                self.movestep(nums, i + 1, len(nums), step)
                step = 0
        # 处理开头处 包含的重复数字
        self.movestep(nums, 0, len(nums), step)  # 如果step不为0， 说明开头就包含重复数字
        return len(nums)

    # 内存最少
    # 双指针方法，注意空间复杂度为O(1)
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了90.53%的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了84.19%的用户
    """

    def removeDuplicates3(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        # nums 长度 i+1
        # 不考虑之后的重复部分，可以不用pop，
        # 但是奇怪的是多执行一段操作，pop之后，执行时间变短，内存消耗也变小
        while len(nums) > (i + 1):
            nums.pop()
        return i + 1

    # 发现重复就执行nums.pop()
    """
    执行用时：76 ms, 在所有 Python3 提交中击败了14.23%的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了37.74%的用户
    """

    def removeDuplicates4(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        #         # i -= 1  # 此操作在for循环中不起任何作用，如i= 0， i-1 = -1,在进入循环的时候，i= 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)
            else:
                i += 1
        return len(nums)


# nums: List[int] = [1,1]
nums: List[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
s = Solution()
l = s.removeDuplicates1(nums)
print("{}, nums = {}".format(l, nums))
