"""
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。

 

示例 1：

输入：flowerbed = [1,0,0,0,1], n = 1
输出：true
示例 2：

输入：flowerbed = [1,0,0,0,1], n = 2
输出：false
 

提示：

1 <= flowerbed.length <= 2 * 104
flowerbed[i] 为 0 或 1
flowerbed 中不存在相邻的两朵花
0 <= n <= flowerbed.length
"""

# 我的题解：贪心
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        left = -1
        for i in range(l + 1):
            if i < l and flowerbed[i] == 0:  # 注意边界条件
                continue
            right = i
            if left == -1 and i == l:  # 注意边界
                num = (right - left) // 2  # 注意计算方式
            elif left == -1 or i == l:  # 注意边界
                num = (right - left - 1) // 2
            else:
                num = (right - left - 1 - 1) // 2
            # print(i, right, left, num, n)
            n -= num
            if n <= 0:
                return True
            left = right  # 注意左边界
        return False

# 官方题解：贪心
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, m, prev = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev < 0:
                    count += i // 2
                else:
                    count += (i - prev - 2) // 2
                if count >= n:
                    return True
                prev = i
        
        if prev < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev - 1) // 2
        
        return count >= n
