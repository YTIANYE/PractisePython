from typing import List
from collections import Counter


class Solution:
    """哈希表方法：使用Counter快速创建哈希表"""

    def singleNumber2(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        print(hashmap)      # Counter({1: 2, 0: 1, 2: 1})       # 默认出现次数多的，会放在前面
        result = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                result.append(k)
        return result


s = Solution()
nums = [0, 1, 1, 2]
print(sorted(nums))  # 28 33
print(s.singleNumber2(nums))
