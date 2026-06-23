# 测试heapq
import heapq

# 创建一个空的最小堆
min_heap = []
# 向最小堆中添加元素
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8) 
heapq.heappush(min_heap, 1)
# 输出最小堆中的元素
print("最小堆中的元素:", min_heap) # 输出: 最小堆中的元素: [1, 2, 8, 5]
# 获取最小堆中的最小元素
min_element = min_heap[0]
print("最小堆中的最小元素:", min_element) # 输出: 最小堆中的最小元素: 1
# 从最小堆中弹出最小元素
popped_element = heapq.heappop(min_heap)
print("弹出的最小元素:", popped_element) # 输出: 弹出的最小元素: 1
print("弹出最小元素后的最小堆:", min_heap) # 输出: 弹出最小元素后的最小堆: [2, 5, 8]
# 将最小堆转换为最大堆
max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)
print("最大堆中的元素:", max_heap) # 输出: 最大堆中的元素: [-8, -5, -2]
# 获取最大堆中的最大元素
max_element = -max_heap[0]
print("最大堆中的最大元素:", max_element) # 输出: 最大堆中的最大元素: 8
# 从最大堆中弹出最大元素
popped_max_element = -heapq.heappop(max_heap)
print("弹出的最大元素:", popped_max_element) # 输出: 弹出的最大元素: 8
print("弹出最大元素后的最大堆:", max_heap) # 输出: 弹出最大元素后的最大堆: [-5, -2]
