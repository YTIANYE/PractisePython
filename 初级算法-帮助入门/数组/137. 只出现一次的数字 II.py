""""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,3,2]
输出: 3
"""
from collections import Counter
from typing import List


class Solution:

    """
    执行用时：32 ms, 在所有 Python3 提交中击败了98.67% 的用户
    内存消耗：16.2 MB, 在所有 Python3 提交中击败了10.42% 的用户
    """

    def singleNumber1(self, nums: List[int]) -> int:

        return int((sum(set(nums)) * 3 - sum(nums)) / 2)

    """官方题解一 注意Counter的用法 """
    def singleNumber2(self, nums):
        hashmap = Counter(nums)
        # print(hashmap)  # Counter({2: 3, 3: 1})
        for k in hashmap.keys():
            if hashmap[k] == 1:
                return k

    """官方题解二 异或解决"""
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了49.88% 的用户
    内存消耗：15.6 MB, 在所有 Python3 提交中击败了94.17% 的用户
    """

    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once



s = Solution()
nums = [2,2,3,2]
num = s.singleNumber(nums)
print(num)