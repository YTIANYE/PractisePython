"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
示例 2：

输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
示例 3：

输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
 

提示：

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
"""

# 官方题解： 枚举3
from sortedcontainers import SortedList  # pyright: ignore[reportMissingImports]
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # 数组长度小于3不可能存在i<j<k
        if n < 3:
            return False
        
        # j左边最小的值，也就是最优的"1"
        left_min = nums[0]
        # j从1开始，j右边从下标2开始，初始化右侧有序集合
        right_all = SortedList(nums[2:])
        
        # j的取值范围 [1, n-2]，j后面至少留有一个k
        for j in range(1, n - 1):
            # 当前j可以当做峰值3
            if left_min < nums[j]:
                # 找到第一个 > left_min 的下标
                index = right_all.bisect_right(left_min)
                # 该位置元素存在 并且 小于峰值nums[j]，即找到合法k
                if index < len(right_all) and right_all[index] < nums[j]:
                    return True
            # 更新左边最小值
            left_min = min(left_min, nums[j])
            # j前进一格，nums[j+1]不再属于j的右侧区间，移除
            right_all.remove(nums[j + 1])

        return False

# 官方题解：单调栈
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # 初始化最右侧元素，它是候选的2
        candidate_k = [nums[n - 1]]
        # max_k：已经确认可用、真正合格的2的最大值
        max_k = float("-inf")

        # 从右往左枚举，nums[i] 尝试充当1
        for i in range(n - 2, -1, -1):
            # 步骤一：当前nums[i]可以作为1，找到模式
            if nums[i] < max_k:
                return True
            
            # 步骤二：nums[i]充当峰值3；弹出所有小于它的候选‑2
            while candidate_k and nums[i] > candidate_k[-1]:
                max_k = candidate_k[-1]
                candidate_k.pop()
            
            # 步骤三：合格才压入，作为之后左边元素的候选‑2
            if nums[i] > max_k:
                candidate_k.append(nums[i])

        return False