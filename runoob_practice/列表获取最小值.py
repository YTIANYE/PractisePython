list1 = [10, 20, 4, 45, 99]

#   默认由小到大排序
list1.sort()

#   [4]
print(list1[:1])

#   4
print(*list1[:1])
print(list1[0])

#   使用min()函数
print("最小元素为:", min(list1))


#   移除某一特定值的元素
list1.remove(4)
print(list1)