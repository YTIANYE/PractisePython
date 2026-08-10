"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

# 我实现的官方题解：DFS + 剪枝
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        nums.sort()  # 注意先排序
        self.vis = [False] * n

        def dfs(index, temp):
            if index == n:
                self.res.append(temp[:])
                return
            for i in range(n):
                if self.vis[i] or (
                    # 当左边相同元素还没有被使用的时候，现在就不要选右边这个重复数字。
                    i > 0 and nums[i] == nums[i - 1] and not self.vis[i - 1]
                ):
                    continue
                self.vis[i] = True
                temp.append(nums[i])
                dfs(index + 1, temp)
                temp.pop(-1)
                self.vis[i] = False

        dfs(0, [])
        return self.res
