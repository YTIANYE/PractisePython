"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
from typing import List


class Solution:
    # 我的题解: 动态规划 滚动数组
    """
    记录已知范围内的后三个位置pre, p, post,
    记录分别以pre, p, post 结尾的最大金额pre_max, p_max, post_max
    当有新的nums[i]加入时，以i结尾的i_max = max(p_max, pre_max) + nums[i]
        不可能是post_max + nums[i],因为post和i相邻
        不考虑以pre前一个结点j结尾的 j_max 与 nums[i]相加,这样会跳过一个p( p>= 0)
    pre_max, p_max, post_max 依次后移
    从以上三者中选出最大的max_sum,作为i位置之前（包含i）的最大金额
    """
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了60.85%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了32.22%的用户
    """

    def rob1(self, nums: List[int]) -> int:
        if len(nums) < 4:
            if len(nums) == 3:
                return max(nums[1], nums[0] + nums[2])
            return max(nums)
        pre_max = nums[0]  # 以pre为结尾，之前（包含pre）的最大金额
        p_max = max(nums[0], nums[1])  # 以p为结尾，之前的最大金额
        post_max = nums[0] + nums[2]
        max_sum = max(p_max, pre_max, post_max)  # 当前最大金额
        # pre p post i
        for i in range(3, len(nums)):
            i_max = max(p_max, pre_max) + nums[i]
            pre_max, p_max, post_max = p_max, post_max, i_max
            max_sum = max(pre_max, p_max, post_max)
        return max_sum

    # 官方题解：动态规划、滚动数组
    """
    frist, second分别记录倒数第二个结点和最后一个结点之前的最大金额，
    遍历到新的一个结点i时，这一节点之前的最大金额为max(first + nums[i], second)
    滚动迭代 first second
    """

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        first, second = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            first, second = second, max(first + nums[i], second)
        return second


s = Solution()
# nums = [1, 2, 3, 1]     # 4
# nums = [2, 7, 9, 3, 1]        # 12
# nums = [2, 3, 2]        # 4
# nums = [1, 1, 1, 1]     #2
# nums = [1, 7, 9, 4]     # 11
# nums = [1, 3, 1, 3, 100]        # 103
# nums = [0]
# nums = [1, 1, 1, 2]
# nums = [100, 1, 1, 100]     # 200
# i   first   second
#     100     100
# 2   100     101
# 3   101     200
print(s.rob(nums))
