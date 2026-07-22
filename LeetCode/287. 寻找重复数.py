"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

 

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3
 

 

提示：

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
 

进阶：

如何证明 nums 中至少存在一个重复的数字?
你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
"""

# 官方题解——双指针 
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# 我的题解——二分查找
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 1, n - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for x in nums:
                if x <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans

# 官方题解——位运算
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        bit_max = 31
        while (n - 1) >> bit_max == 0:
            bit_max -= 1
        
        for bit in range(bit_max + 1):
            x = y = 0
            mask = 1 << bit
            # print(mask)
            for i in range(n):
                if nums[i] & mask:
                    x += 1
                if i >= 1 and i & mask:
                    y += 1
            if x > y:
                ans |= mask
        return ans