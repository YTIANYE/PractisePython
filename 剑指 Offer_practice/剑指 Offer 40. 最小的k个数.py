"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i]<= 10000
"""
from typing import List
import heapq


class Solution:

    # 官方题解：
    """
    执行用时：56 ms, 在所有 Python3 提交中击败了66.98%的用户
    内存消耗：16.6 MB, 在所有 Python3 提交中击败了21.44%的用户
    """

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if len(arr) == 0 or k == 0:
            return []

        hp = [num * -1 for num in arr[:k]]
        heapq.heapify(hp)  # 初始化堆

        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)  # 取出顶部值
                heapq.heappush(hp, -arr[i])  # 加入新的值

        res = [-num for num in hp]
        return res


if __name__ == "__main__":
    num = [0, 1, 2, 1]
    k = 2
    s = Solution()
    print(s.getLeastNumbers(num, k))
