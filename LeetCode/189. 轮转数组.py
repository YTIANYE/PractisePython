"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

进阶：

尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return None
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]   # nums[:] 表示修改原列表的内容，而不是重新赋值

class Solution_1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def get_gcd(n, k):
            while k != 0:
                k, n = n % k, k
            return n

        n = len(nums)
        k = k % n
        if k == 0 or n <= 1:    # 注意循环条件
            return

        start = 0
        count = 0
        while count < n:
            pre_val = nums[start]
            cur = start  # 关键修正：从start本身开始，而非start+k
            while True:
                nex = (cur + k) % n  # 计算下一个位置
                # 核心：把pre_val写入nex位置，保存nex原值，更新cur
                nums[nex], pre_val = pre_val, nums[nex]
                cur = nex
                count += 1
                # 回到起点时，当前环处理完毕
                if cur == start:
                    break
            start += 1


from typing import List

class Solution_2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 最大公约数
        def get_gcd(n, k):
            while k != 0:
                k, n = n % k, k
            return n

        n = len(nums)
        k = k % n  # 先处理k，再判断是否为0（避免k=0但n=0的情况）
        if k == 0:
            return

        gcd = get_gcd(n, k)
        for i in range(gcd):
            # 方式二
            pre_num = nums[i]  # 保存当前环的初始值
            cur = i
            while True:
                next_idx = (cur + k) % n  
                # 核心修复：把pre_num放到next_idx位置，原next_idx值存到pre_num，更新cur
                nums[next_idx], pre_num, cur = pre_num, nums[next_idx], next_idx
                # 回到起点时终止循环
                if cur == i:
                    break

        # # 方式一
        # for i in range(gcd):
        #     pre = nums[i]
        #     j = (i + k) % n
        #     while j != i:
        #         nums[j], pre = pre, nums[j]
        #         j = (j + k) % n
        #     # 循环结束时j==i，无需额外赋值