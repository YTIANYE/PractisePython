"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
示例 1：
输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
"""
from collections import Counter
from functools import reduce
from typing import List


class Solution:

    """
    方案失败（如果不进行排序的话）
    原因：[1,2,1,3,2,5]，折半过程中会将一对数字分开，2会被识别出来
    """
    """
    执行用时：60 ms, 在所有 Python3 提交中击败了15.84% 的用户
    内存消耗：15.8 MB, 在所有 Python3 提交中击败了68.32% 的用户
    """
    # 返回nums一段上所有数字的 异或 结果
    def fun_xor(self, nums: List[int], left: int, right: int) -> int:
        return reduce(lambda x, y: x ^ y, nums[left:right+1])

    def fun_zheban(self, nums: List[int], left:int, right:int) -> List[int]:
        """
        结合折半查找
        当right-left > 1
            将数据折半，注意避免在两个相同的数中间切开
            先取数组的左半边，计算所有数字的异或结果first
                若first结果为 0，则两个数均在右半边，重新查找右半边
                若first结果不为0，取nums的右半边，计算所有数字的异或结果second
                    若结果second为0，则两个数均在左半边，重新查找左半边
                    若second结果不为0，则两个数分列左右两半，分别为first，second
        当right-left == 1时，left和right的位置就是这两个数
        """
        if right - left > 1:
            mid = (right + left)//2
            """
            # 注释A
            # 保证平分时两边都是偶数个数。如果两边都是奇数，在两边会分别会产生新的不重复的数，如[1,1,2,    2,3,5]
            # 保证两边的数组都是偶数的时候，也会产生新的不重复的数，如[1,2,2,5]
            # 所以注释A部分需要结合注释B才能解决问题，不如在求mid初始就对mid进行调整
            # [1,2,2,3,3,5]
            if int((mid - left + 1) % 2) == 1:
                mid += 1
            """
            # 恰好折半处产生不重复的数分列两边，即折半处两个数相等，如[1, 2, 2, 3,     3, 4, 4, 5]
            if nums[mid] == nums[mid + 1]:
                mid += 1
            first = self.fun_xor(nums, left, mid)
            if first == 0:
                # 注意 mid+1 避免两次传入 nums[mid]
                # 注意递归调用时，调用自身需要加 return
                return self.fun_zheban(nums, mid + 1, right)
            else:
                # 注意 mid+1 避免两次传入 nums[mid]
                second = self.fun_xor(nums, mid + 1, right)
                if second == 0:
                    return self.fun_zheban(nums, left, mid)
                else:
                    """
                    # 注释B
                    # else 表示恰好折半处产生不重复的数分列两边，即折半处两个数相等，如[1,1,2,2,3,4,     4,5,9,9]
                    if nums[mid] != nums[mid + 1]:
                        return [first, second]
                    else:
                        first = self.fun_xor(nums, left, mid - 1)
                        second = self.fun_xor(nums, mid, right)
                        return [first, second]                    
                    """
                    return [first, second]

        else:   # right-left == 1
            return [nums[left], nums[right]]

    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        # if 0 in nums:     # 注意，特殊情况是数组中只有一个0，有两个0无所谓
        if nums.count(0) == 1:
            return [0, self.fun_xor(nums, 0, len(nums) - 1)]
        else:
            return self.fun_zheban(nums, 0, len(nums) - 1)

    """哈希表方法：使用Counter"""
    def singleNumber2(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        result = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                result.append(k)
        return result

    """官方题解"""
    """我的不足：想到了求所有数字异或的结果result，以及将两个数分开就变成了第一种情况，且需要遍历两次，但是没有找到合适的分组方法和使用result的方法"""
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了29.01% 的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了85.97% 的用户
    """
    def singleNumber3(self, nums: List[int]) -> List[int]:
        # 求得所有数字异或结果，即两个数a b 的异或结果
        result = reduce(lambda x, y: x ^ y, nums)
        # result 中为1的位标识 a b 不等的位
        temp = 1    # 记录result中最右边的为1的位
        while temp & result == 0:
            temp <<= 1
        a = b = 0
        for num in nums:
            # 相同的数一定会被分在同一组中
            # 如果该位为0就分到第一组，否则就分到第二组
            """
            这个方法在 xi=1 的时候 a 和 b 不被分在同一组，
            因为 xi=1 表示 ai 和 bi 不等，
            根据这个方法的定义「如果该位为 0 就分到第一组，否则就分到第二组」可以知道它们被分进了两组，所以满足了条件 1。
            """
            if temp & num:
                a ^= num
            else:
                b ^= num
        return [a, b]




s = Solution()
# nums = [1,2,1,3,2,5,4,4]
# nums = [1,2,1,3,2,5]
# nums = [1,1,2,2,3,5]
# nums = [1193730082,587035181,-814709193,1676831308,-511259610,284593787,-2058511940,1970250135,-814709193,-1435587299,1308886332,-1435587299,1676831308,1403943960,-421534159,-528369977,-2058511940,1636287980,-1874234027,197290672,1976318504,-511259610,1308886332,336663447,1636287980,197290672,1970250135,1976318504,959128864,284593787,-528369977,-1874234027,587035181,-421534159,-786223891,933046536,959112204,336663447,933046536,959112204,1193730082,-786223891]
# nums = [1,2,2,3,3,4,4,5]
nums = [0,1,1,2]
# nums = [0,0,1,2]
# nums = [-1,1,1,2]
print(sorted(nums)) # 28 33
print(s.singleNumber(nums))

