"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果

示例：

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]

提示：

1 <= nums.length <= 200
-106 <= nums[i] <= 106
nums 中的所有元素都是 唯一的
最多可以调用 5 * 104 次 reset 和 shuffle

"""
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    # 我的题解：从nums中随机选一个数后删除，不断生成新的snums
    """
    执行用时：164 ms, 在所有 Python3 提交中击败了86.53%的用户
    内存消耗：20.2 MB, 在所有 Python3 提交中击败了46.21%的用户
    """

    def shuffle1(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # nums = [num for num in self.nums]
        nums = list(self.nums)
        print(nums)
        # 如果是nums = self.nums这种方式，地址一样，pop之后self.nums也会变空
        snums = []
        while nums:
            index = int(len(nums) * random.random())
            if nums[index] not in snums:
                snums.append(nums[index])
                nums.pop(index)
        return snums

    # 我实现的 官方题解：采用交换的方式，时间复杂度更小O(n)
    """
    执行用时：196 ms, 在所有 Python3 提交中击败了56.99%的用户
    内存消耗：20.4 MB, 在所有 Python3 提交中击败了11.91%的用户
    """

    def shuffle(self) -> List[int]:
        snums = list(self.nums)
        for i in range(len(snums)):
            index = random.randrange(i, len(snums))
            snums[i], snums[index] = snums[index], snums[i]
        return snums


if __name__ == "__main__":
    string = input("输入命令(Solution)：")
    if string == "Solution":
        str_nums = input("输入nums：")
        nums = []
        for str in str_nums:
            if str != " ":
                nums.append(int(str))
        solution = Solution(nums)
    while True:
        string = input("输入命令(shuffle,reset)：")
        if string == "shuffle":
            print(solution.shuffle())
        elif string == "reset":
            print(solution.reset())
