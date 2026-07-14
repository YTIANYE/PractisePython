"""
定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 

 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

# 我实现的官方题解
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def find_k(k):
            left1, left2 = 0, 0
            while True:
                print(left1, left2, k, m , n)
                if left1 == m:  # 注意边界条件
                    return nums2[left2 + k - 1] # 注意返回值
                if left2 == n:
                    return nums1[left1 + k - 1]
                if k == 1:
                    return min(nums1[left1], nums2[left2])

                i1 = min(left1 + k // 2 - 1, m - 1)  # 防止越界
                i2 = min(left2 + k // 2 - 1, n - 1)  # 防止越界
                if nums1[i1] <= nums2[i2]:
                    k -= i1 - left1 + 1 # 先计算k
                    left1 = i1 + 1
                else:
                    k -= i2 - left2 + 1
                    left2 = i2 + 1

        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            k = (m + n + 1) // 2
            return find_k(k)
        else:
            k1 = (m + n) // 2
            k2 = k1 + 1
            return (find_k(k1) + find_k(k2)) / 2
