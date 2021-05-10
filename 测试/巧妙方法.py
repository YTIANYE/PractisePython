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

    # 两种不同的方式，在list中初始化多个字典
    def dictinlist(self):
        rows = [{}] * 9     # 这里的 * 9 是把{}这个对象复制了9次，更改值的时候，每个被复制的对象也会跟随更改
        columns = [{} for i in range(9)]  # [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        print(rows)
        print(columns)
        # 造成这样的结果是因为两者的初始化不一样，我的天呀，原来是这样。
        rows[0][0] = 1  # 每一个字典都加入了，例如[{0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}]
        columns[0][0] = 1  # 只是一个字典中加入了，
        print(rows)         # [{0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}, {0: 1}]
        print(columns)      # [{0: 1}, {}, {}, {}, {}, {}, {}, {}, {}]

s = Solution()

# nums = [0, 1, 1, 2]
# print(sorted(nums))  # 28 33
# print(s.singleNumber2(nums))

s.dictinlist()
