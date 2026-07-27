"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        print(nums)
        n = len(nums)
        res = []
        for i in range(0, n - 2):
            # 避免数值重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            p, q = i + 1, n - 1
            while p < q:
                he = nums[i] + nums[p] + nums[q]
                if he > 0:
                    # 避免数值重复
                    while p < q and nums[q] == nums[q-1]:
                        q -= 1
                    q -= 1
                elif he < 0:
                    # 避免数值重复
                    while p < q and nums[p] == nums[p+1]:
                        p += 1
                    p += 1 # 注意这个while如果没进去，没有当前条件，上层循环就是死循环
                else:
                    li = [nums[i], nums[p], nums[q]]
                    res.append(li) # 直接append,不要赋值
                    print(i, p, q)
                    # 避免数值重复
                    while p < q and nums[q] == nums[q-1]:
                        q -= 1
                    q -= 1

        return res
