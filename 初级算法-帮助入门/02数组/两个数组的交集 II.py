"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]

说明：
    输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
    我们可以不考虑输出结果的顺序。
进阶：
    如果给定的数组已经排好序呢？你将如何优化你的算法？
    如果 nums1 的大小比 nums2 小很多，哪种方法更优？
    如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？     答：如果 nums2的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中。那么就无法高效地对 nums2进行排序，因此推荐使用方法一而不是方法二。在方法一中，nums2 只关系到查询操作，因此每次读取 nums2 中的一部分数据，并进行处理即可。
"""
from typing import List
from collections import Counter

class Solution:

    # 我的方法
    """
    执行用时：80 ms, 在所有 Python3 提交中击败了13.74% 的用户
    内存消耗：14.7 MB, 在所有 Python3 提交中击败了95.85% 的用户
    """
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        常用函数：
        list.count(obj) 统计某个元素在列表中出现的次数
        """
        # 集合
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set1 & set2      # 取集合的交集
        nums = []
        for i in set3:  # 集合无序，不能采用set3[i]的形式获取值
            n1 = nums1.count(i)
            n2 = nums2.count(i)
            n = min(n1, n2)  # 次数
            for j in range(0, n):  # 注意加上range 才是范围，否则是元组
                nums.append(i)
        # 注意这是一个函数，要返回值，不是打印 print(nums),否则提交结果的时候是null
        return nums

    # 我的方法
    """
    执行用时：80 ms, 在所有 Python3 提交中击败了13.74% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了11.35% 的用户
    """
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = Counter(nums1)
        hash2 = Counter(nums2)
        nums = []
        for i in hash1.keys():
            for j in hash2.keys():
                if i == j:
                    for k in range(min(hash1[i], hash2[j])):
                        nums.append(i)
        return nums

    # 我的方法
    """
    intersect2 改进版，集合求交集代替两层循环，大幅度提高运行速度
    执行用时：32 ms, 在所有 Python3 提交中击败了99.44% 的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.89% 的用户
    """
    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = Counter(nums1)
        hash2 = Counter(nums2)
        nums = []
        s = set(hash1.keys()) & set(hash2.keys())
        for i in s:
            for k in range(min(hash1[i], hash2[i])):
                nums.append(i)
        return nums

    # 官方题解： 哈希表方法   源代码
    """
    执行用时：48 ms, 在所有 Python3 提交中击败了73.05% 的用户
    内存消耗：14.7 MB, 在所有 Python3 提交中击败了97.33% 的用户
    """
    def intersect4(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，然后遍历第二个数组，
        对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。

        为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，然后遍历较长的数组得到交集。
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        m = Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            # if (count := m.get(num, 0)) > 0:        # := 海象运算符，可在表达式内部为变量赋值，Python3.8版本新增运算符
            if (m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    # 我对官方题解的实现
    """
    执行用时：56 ms, 在所有 Python3 提交中击败了54.02% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了44.27% 的用户
    """
    def intersect5(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)     # 保证nums1是最短的那个
        n = Counter(nums1)
        nums = []
        for num in nums2:
            if n[num] > 0:
                nums.append(num)
                n[num] -= 1
                if n[num] == 0:
                    n.pop(num)
        return nums

    # 我的题解 双指针
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了84.84% 的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了36.87% 的用户
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        nums = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                nums.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return nums


# 测试hash排序情况        # 默认出现次数多的，会放在前面
# nums1 = [4, 9, 5, 5]
# nums2 = [9, 4, 9, 8, 4, 3, 3, 3]

# nums1 = [4, 9, 5]
# nums2 = [9, 4, 9, 8, 4]
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
s = Solution()
print(s.intersect(nums1, nums2))

