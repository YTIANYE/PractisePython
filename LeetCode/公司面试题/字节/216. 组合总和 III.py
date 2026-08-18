"""
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：

只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

 

示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
解释:
1 + 2 + 4 = 7
没有其他符合的组合了。
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
解释:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
没有其他符合的组合了。
示例 3:

输入: k = 4, n = 1
输出: []
解释: 不存在有效的组合。
在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
 

提示:

2 <= k <= 9
1 <= n <= 60
"""

# 我的题解：改良版
from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        
        def dfs(he, count, arr, index):
            if count == 0 and he == n:
                res.append(arr[:])
                return 
            # ==========新增两条剪枝==========
            if he > n:
                return
            # 剩余可选数字不够选出count个
            # 当前最后选到index，最多还能选 9 - index 个数字
            if 9 - index < count:
                return
            # ================================
            for i in range(index+1, 10):
                arr.append(i)
                dfs(he + i, count - 1, arr, i)
                arr.pop(-1)
        
        dfs(0, k, [], 0)
        return res


# 我的题解：回溯 DFS
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        nums = [i for i in range(0, 10)]
        def dfs(he, count, arr, index):
            if count == 0 and he == n:
                t_arr = arr[:]
                res.append(t_arr)
                return 
            if count == 0:
                return 
            if he == n:
                return 
            for i in range(index+1, 10):
                he += nums[i]
                count -= 1 
                arr.append(nums[i])
                dfs(he, count, arr, i)
                arr.pop(-1)
                count += 1
                he -= nums[i]
        dfs(0, k, [], 0)
        return res 
            
# 官方题解：回溯 DFS
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        temp = []

        def dfs(cur: int, rest: int) -> None:
            # 找到一组合法答案
            if len(temp) == k and rest == 0:
                ans.append(temp.copy())
                return
            # 剪枝条件
            # len(temp)+10‑cur < k：剩下可选数字不够凑齐k个
            # rest < 0：和已经超了
            if len(temp) + 10 - cur < k or rest < 0:
                return
            
            # 方案1：不选当前数字 cur
            dfs(cur + 1, rest)
            
            # 方案2：选当前数字 cur
            temp.append(cur)
            dfs(cur + 1, rest - cur)
            temp.pop() # 回溯

        dfs(1, n)
        return ans
