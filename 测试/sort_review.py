"""
Python sort / sorted 笔试面试备考笔记
Author: 备考整理
考点：原地vs新列表、key、reverse、稳定排序、Timsort、多字段排序、坑点
"""

# ===================== 1. 基础区分 =====================
# list.sort()
# - 原地修改原列表，返回 None
# - 仅list对象可用
lst = [3, 1, 4, 2]
res = lst.sort()
print(lst)    # [1, 2, 3, 4] 原列表被修改
print(res)    # None，不要写 lst = lst.sort()

# sorted(iterable)
# - 返回新列表，原数据不变
# - 支持所有可迭代对象：list/tuple/str/set/dict
lst = [3, 1, 4, 2]
new_lst = sorted(lst)
print(lst)       # [3, 1, 4, 2]
print(new_lst)   # [1, 2, 3, 4]

# 通用参数：key=None, reverse=False
# reverse=True -> 降序；reverse=False -> 默认升序


# ===================== 2. key 高频考点 =====================
# key=函数：对每个元素执行函数，用返回值参与排序，不修改原元素
# ❌ key=func()  错误！不要加括号
# ✅ key=func    正确，传函数对象

words = ["apple", "hi", "banana"]
res1 = sorted(words, key=lambda x: len(x))
print("按长度排序:", res1)

data = [(1, 9), (2, 3), (3, 5)]
res2 = sorted(data, key=lambda x: x[1])
print("元组按第2项排序:", res2)

arr = ["Banana", "apple", "Cherry"]
res3 = sorted(arr, key=lambda x: x.lower())
print("忽略大小写排序:", res3)


# ===================== 3. 多条件排序（笔试高频） =====================
# lambda 返回元组，依次比较；负号实现单个字段降序
students = [("zhangsan", 20, 90), ("lisi", 18, 90), ("wangwu",19,85)]
# 规则：分数升序，分数相同则年龄降序
res4 = sorted(students, key=lambda x: (x[2], -x[1]))
print("多条件排序:", res4)


# ===================== 4. 底层&性质（面试口述） =====================
"""
算法：Timsort（归并+插入混合排序）
时间复杂度：O(n log n)
稳定排序：key相等的元素，保留原始相对顺序
空间：
    list.sort() : O(log n)
    sorted()    : O(n) 新建列表
"""


# ===================== 5. 高频坑点（写代码必看） =====================
"""
1. lst = lst.sort() → lst 变成 None，经典bug
2. 列表内类型不一致，如 [1,"a"]，直接报错
3. key只改变比较值，不会修改原始元素
4. 稳定排序判断依据是key，不是元素本身
"""


# ===================== 一句话速记 =====================
"""
sort原地返None，sorted生成新列表；
key取比较值，元组做多条件；
Timsort稳定，复杂度nlogn。
"""
