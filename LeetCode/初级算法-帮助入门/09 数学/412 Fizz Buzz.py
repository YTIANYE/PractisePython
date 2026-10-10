"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果n是3的倍数，输出“Fizz”；

2. 如果n是5的倍数，输出“Buzz”；

3.如果n同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""
from typing import List


class Solution:
    # 我的题解
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了72.02%的用户
    内存消耗：15.3 MB, 在所有 Python3 提交中击败了48.67%的用户
    """
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

s = Solution()
n = 15
print(s.fizzBuzz(n))