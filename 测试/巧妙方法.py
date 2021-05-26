from typing import List
from collections import Counter


class Solution:
    """哈希表方法：使用Counter快速创建哈希表"""

    def singleNumber2(self, nums: List[int]) -> List[int]:
        hashmap = Counter(nums)
        print(hashmap)      # Counter({1: 2, 0: 1, 2: 1})       # 默认出现次数多的，会放在前面    # 若传入字符串，则统计字符串中字母出现次数
        result = []
        for k in hashmap.keys():
            if hashmap[k] == 1:
                result.append(k)
        return result

    """ 两种不同的方式，在list中初始化多个字典 """
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

    """（for .. in .. if）形式的用法      快速对比回文串 """
    def isPalindrome(self) -> bool:
        s = "A man, a plan, a canal: Panama"
        # isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False

        sgood_rev = "".join(ch.lower() for ch in s if ch.isalnum())     # 这语句真棒  “”,join 值得学习，同时完成是不是数字或字母的判断和小写化
        return sgood_rev == sgood_rev[::-1]         # 这个正反比对太简洁了

    """ 重复元素判定 ,使用 set() 函数来移除所有重复元素 """
    def all_unique(self, lst):
        return len(lst) == len(set(lst))

    """ 字符元素组成判定, 检查两个字符串的组成元素是不是一样的"""
    def anagram(self, first, second):
        return Counter(first) == Counter(second)

    """ 打印 N 次字符串 """
    def printNstring(self):
        n = 2
        s = "Programming"
        print(s * n)

    """ 逗号连接 .join()用法 """
    def joinFun(self):
        hobbies = ["basketball", "football", "swimming"]
        print("My hobbies are: " + ", ".join(hobbies))

    """ 通过递归的方式将列表的嵌套展开为单个列表 """
    def spreadFun(self):
        def spread(arg):
            ret = []
            for i in arg:
                if isinstance(i, list):
                    ret.extend(i)
                else:
                    ret.append(i)
            return ret
        def deep_flatten(lst):
            result = []
            result.extend(
                spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
            return result
        print(deep_flatten([1, [2], [[3], 4], 5]))  # [1,2,3,4,5]

    """ 链式函数调用 : 在一行代码内调用多个函数。 """
    def arrFun(self):
        def add(a, b):
            return a + b
        def subtract(a, b):
            return a - b
        a, b = 4, 5
        print((subtract if a > b else add)(a, b))  # 9

    """ 使用枚举遍历 """
    def enumerateFun(self):
        l = ["a", "b", "c", "d"]
        for index, element in enumerate(l):
            print("Value", element, "Index ", index, )
            # ('Value', 'a', 'Index ', 0)
            # ('Value', 'b', 'Index ', 1)
            # ('Value', 'c', 'Index ', 2)
            # ('Value', 'd', 'Index ', 3)

    """ 元素频率， 下面的方法会根据元素频率取列表中最常见的元素 """
    def frequentFun(self):
        def most_frequent(l):
            return max(set(l), key=l.count)
        l = [1, 2, 1, 2, 3, 2, 1, 4, 2]
        print(most_frequent(l))

    """ 展开列表 将列表内的所有元素，包括子列表，都展开成一个列表。"""
    def spreadFun(self):
        def spread(arg):
            ret = []
            for i in arg:
                if isinstance(i, list):
                    ret.extend(i)
                else:
                    ret.append(i)
            return ret
        print(spread([1, 2, 3, [4, 5, 6], [7], 8, 9]))  # [1,2,3,4,5,6,7,8,9]


s = Solution()
s.spreadFun()
