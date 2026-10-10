"""
字节跳动夏令营2021第二轮笔试题t3
题目大概描述：

有一排座位和n个学生，每个学生依次挑选座位，每位同学不能挨着坐
每个学生选取 所有连续空座位中最长的 入座
入座时选取中间的位置，如果有两个都是中间的位置，选左边的

满足n个学生的要求，求最少需要多少个座位？

# 手动举例子
# 1个学生 1个座位
# 1
# 2个学生 4个座位
# 0101
# 3 5
# 10101
# 4 8
# 01010101
# 5 11
# 10100100101
# 6 13
# 1010101001010
# 7 14
# 10101010101010
# 8 16
# 0101010101010101
# 9个学生 23个座位
# 1010010010 0100100100 101
# 22个不行 0100100100 1001001001 01

"""
import sys
from typing import List

if __name__ == "__main__":

    # 检测n个学生， len(arr)个座位是不是可以满足
    def test(n: int, arr: List[int]) -> bool:
        # n个学生
        if n == 0:
            return True

        # 找出最长的连续空座位
        first = -1  # 第一个空座位出现的下标
        last = -1  # 最后一个空座出现的下标
        tag = 0
        max = [0, -1]  # 最长的连续空座位下标，  注意座位数要 b-a+1
        # 可能会有多个最大空白，都需要存起来
        max_arr = []

        for i in range(0, len(arr)):
            if arr[i] == 0 and tag == 0:
                if i != len(arr) - 1:
                    first = last = i
                    tag = 1  # 开始找
                else:  # 开始找的位置是最后一个位置，且这个位置是空位置
                    if max[1] - max[0] < 0:  # 之前没有找到任何最大空白
                        max[0] = max[1] = i
                        max_arr.append(max)
            elif arr[i] == 0 and tag == 1 and i != len(arr) - 1:
                last += 1
            elif (arr[i] == 1 and tag == 1) or (i == len(arr) - 1 and arr[i] == 0 and tag == 1):
                if i == len(arr) - 1:
                    if arr[i] == 0:
                        last += 1
                tag = 0  # 不找了
                if max[1] - max[0] < last - first:  # 找到了比原来的还长的空白
                    max[0], max[1] = first, last
                    max_arr.clear()
                    max_arr.append(max)
                elif max[1] - max[0] == last - first:  # 找到了一样也是最长的空白
                    max_arr.append([first, last])
            else:
                pass

        if pan_max(max_arr):
            return test(n - 1, arr)
        else:  # 所有最大空白都不满足
            return False


    # 判断max_arr中存的max可不可以放1
    def pan_max(max_arr: List[List[int]]) -> bool:
        # 找到最大连续空白就置为1
        tag = False  # True 表示可以， False表示不可以, 最大空白多个的时候，找到第一个就可以了
        for max in max_arr:
            if (max[1] - max[0] + 1) % 2 == 1:
                mid = (max[0] + max[1]) // 2
                if yanzheng(mid, arr):
                    tag = False
                else:
                    arr[mid] = 1
                    tag = 1
                    break
            else:
                tag1 = tag2 = 1
                mid = (max[0] + max[1]) // 2 + 1
                if yanzheng(mid, arr):  # 后一个不行
                    tag2 = 0
                mid -= 1
                if yanzheng(mid, arr):  # 前一个不行
                    tag1 = 0
                if tag1 == 1:  # 只要前一个可以，就是前一个
                    arr[mid] = 1
                    tag = True
                    break
                elif tag2 == 1:  # 后一个可以
                    arr[mid + 1] = 1
                    tag = True
                    break
                else:  # 都不行
                    tag = False
        return tag


    # 判断一个序列是不是有相邻的1
    def yanzheng(mid: int, arr: List[int]) -> bool:
        arr[mid] = 1
        for i in range(len(arr) - 1):
            if arr[i] == 1 and arr[i + 1] == 1:
                arr[mid] = 0
                return True  # 存在相邻的1
        arr[mid] = 0
        return False  # 不存在相邻的1


    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for n in values:
            # 有n个学生
            i = n
            while True:
                arr = [0] * i  # 座位
                if test(n, arr):
                    print(i)
                    break
                else:
                    i += 1
