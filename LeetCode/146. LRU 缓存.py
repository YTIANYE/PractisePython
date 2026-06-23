"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
"""

# 我的题解（官方题解思路）
class ListNode():
    def __init__(self, key = 0, val = 0, pre = None, next = None):
        self.key =key   #由于要逐出最久未使用关键字，及双向链表最后一个结点，需记录key，移除hash[key]
        self.val = val 
        self.pre = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.hash = {}  # key: key, value: ListNode
        self.capacity = capacity
        self.nums = 0 
        self.head = ListNode(0, 0, None, None)
        self.tail = ListNode(0, 0, None, None)
        self.head.next = self.tail 
        self.tail.pre = self.head 
        

    def get(self, key: int) -> int:
        if key not in self.hash.keys():
            return -1 
        node = self.hash[key]
        self.remove(node)
        self.insert(node)
        return node.val 
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash.keys():
            node = self.hash[key]
            node.val = value 
            self.remove(node)
            self.insert(node)
        else:
            node = ListNode(key, value, None, None)
            self.insert(node)
            if self.nums > self.capacity:
                self.remove(self.tail.pre)
            
        
    def remove(self, node: ListNode):
        # 从双向链表移除
        node.pre.next = node.next 
        node.next.pre = node.pre 
        self.nums -= 1
        self.hash.pop(node.key)
    
    def insert(self, node: ListNode):
        # 插入head后
        node.pre = self.head 
        node.next = self.head.next 
        self.head.next.pre = node 
        self.head.next = node 
        self.nums += 1
        self.hash[node.key] = node   # node.val并不是key

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)