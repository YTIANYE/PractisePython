"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

"""
from typing import List


class Solution:
    # 我的题解
    """
    如示例
    （1）缩小行数范围
    第 0 列，如果target < 10, 表示10之后的所有数都比target大， 由第0列找出上限m_max
    第n-1列，如果target > 19, 表示19之前的所有数都比target小，由第n-1列找出下限m_min
    则所要找的数在(m_min, m_max)中的行里面
    （2）缩小列数范围
    第 0 行，如果target < 15, 表示15之后的所有数都比target大， 由第0行找出上限n_max
    第m-1行，如果target > 18, 表示18之前的所有数都比target小，由第m-1行找出下限n_min
    则要找的数在(n_min, n_max)中的列里面

    可以将两者配合使用，不断缩小查找范围

    依次查找这些行中是否有target

    注意：确定行数范围以及查找target过程中均采用二分查找
    """
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了71.14%的用户
    内存消耗：19 MB, 在所有 Python3 提交中击败了7.97%的用户
    """

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        # 二分查找
        def binary(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:  # nums[mid] == target:
                    return True, left  # 表示找到了target
            return False, left  # 表示没找到terget

        # matrix 为空
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # 小于最小值，大于最大值，直接排除
        m = len(matrix)  # 行数
        n = len(matrix[0])  # 列数
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False

        # 缩小行数范围

        nums1 = [matrix[i][0] for i in range(0, m)]
        nums2 = [matrix[i][n - 1] for i in range(0, m)]
        tag1, m_max = binary(nums1, 0, m - 1, target)
        tag2, m_min = binary(nums2, 0, m - 1, target)
        if tag1 or tag2:        # 首列或者最后一列就有这个数
            return True

        # 缩小列数范围

        nums3 = matrix[m_min]
        nums4 = matrix[m_max - 1]
        tag3, n_max = binary(nums3, 0, n - 1, target)
        tag4, n_min = binary(nums4, 0, n - 1, target)
        if tag3 or tag4:
            return True

        # 按行查找
        for i in range(m_min, m_max):  # 注意 左闭右开
            tag, left = binary(matrix[i], n_min, n_max - 1, target)
            if tag:
                return True
        return False

    # 我的题解
    """
    特性：
    一个数的左面和上面的数均小于该数；
    一个数的右面和下面的数均大于该数；
    """
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了96.81%的用户
    内存消耗：19 MB, 在所有 Python3 提交中击败了18.11%的用户
    """
    def findNumberIn2DArray2(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True
        return False


solu = Solution()
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 1

# matrix = []
# target = 0
print(solu.findNumberIn2DArray(matrix, target))
