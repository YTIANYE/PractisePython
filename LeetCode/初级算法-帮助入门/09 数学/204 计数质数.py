"""
统计所有小于非负整数n的质数的数量。

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

提示：

0 <= n <= 5 * 106
"""


class Solution:
    # 我的题解： 超时
    def countPrimes1(self, n: int) -> int:
        count = 0
        for num in range(2, n):  # 注意题干是小于，不是小于等于
            if self.primes(num):
                count += 1
        return count

    # 判断一个数是不是 质数
    def primes(self, num) -> bool:
        i = 2
        # while i <= num ** 0.5:
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

    # 我实现的 官方题解  埃氏筛
    """
    执行用时：3620 ms, 在所有 Python3 提交中击败了11.38%的用户
    内存消耗：67.3 MB, 在所有 Python3 提交中击败了32.21%的用户
    """

    def countPrimes2(self, n: int) -> int:
        nums = [1 for i in range(n)]
        count = 0
        for i in range(2, n):
            if nums[i] == 1:
                count += 1
            if i * i < n:
                j = i * i
                while j < n:
                    nums[j] = 0
                    j += i  # j += 1 的话不合理
        return count

    # 别人的题解
    # 使用标准的 埃拉托斯特尼 埃氏筛选法 -
    def countPrimes3(self, n: int) -> int:
        isNumPrimes = [True] * n  # 将所有数，展开所有数 标记质数真
        count = 0  # 质数计数器 因为1不是质数 所以 0
        # 遍历2，n 数，判断是否是质数，从2开始对应-质数3 [1,2,3]  1不算质数
        for i in range(2, n):
            if isNumPrimes[i]:
                count += 1
                # 使用埃拉托斯特尼 筛选法进行过滤 将合数去除
                for j in range(i * i, n, i):  # 遍历 i*i  2倍i值 开始，结束n, 步数i (倍数递增)
                    isNumPrimes[j] = False  # 把合数置为 False
        return count

    # 我实现的 官方题解  线性筛
    """
    执行用时：1724 ms, 在所有 Python3 提交中击败了44.10%的用户
    内存消耗：78.1 MB, 在所有 Python3 提交中击败了26.54%的用户
    """
    def countPrimes(self, n: int) -> int:
        primes = []  # 当前得到的质数集合
        nums = [1 for i in range(n)]
        for i in range(2, n):
            if nums[i] == 1:
                primes.append(i)
            # j = 0
            # while j < len(primes) and i * primes[j] < n:
            #     nums[i * primes[j]] = 0
            #     if i % primes[j] == 0:
            #         break
            #     j += 1
            for prime in primes:
                if i * prime < n:
                    nums[i * prime] = 0
                    if i % prime == 0:
                        break
                else:       # 加 else 进行break很重要，及时终止迭代，避免重复进入迭代
                    break
        return len(primes)


s = Solution()
# n = 999983  # 78497
n = 499979      # 41537
# n = 1500000  # 114155
# n = 15
# n = 2
print(s.countPrimes(n))
