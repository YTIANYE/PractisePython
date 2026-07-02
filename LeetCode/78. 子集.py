"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""

# # 我的题解
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#         for i in range(n):
#             num = nums[i]
#             if i == 0:
#                  res = [[], [num]]
#                  continue 
#             len_res= len(res)
#             for j in range(len_res):
#                 t = list(res[j])    # t = res[j][:]这种方式复制，遇到res[j] = []时会报错
#                 t.append(num)
#                 res.append(t)
           
#         return res 


# # 精选题解

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in range(len(nums)):
#             for j in range(len(res)):
#                 res.append(res[j]+[nums[i]])    # a + b：拼接直接返回新 list
#         return res 



 # 官方题解：回溯
 from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []  # 全局临时路径
        
        def dfs(cur):
            # 到达数组末尾，保存当前路径
            if cur == len(nums):
                res.append(list(temp))
                return
            # 分支1：选当前 nums[cur]
            temp.append(nums[cur])
            dfs(cur + 1)
            temp.pop()  # 回溯，撤销选择
            
            # 分支2：不选当前 nums[cur]
            dfs(cur + 1)
        
        dfs(0)
        return res           

            

        