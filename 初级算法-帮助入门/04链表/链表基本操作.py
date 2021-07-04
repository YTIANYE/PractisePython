from xmlrpc.client import Boolean


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""单链表：无头链表"""


class singleLinkList(object):
    """Fun1: 初始化链表"""

    def __init__(self):
        self._head = None

    """Fun2: 判断链表是否为空"""

    def isEmpty(self):
        return self._head is None

    """Fun3: 链表长度"""

    def lenght(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    """Fun4: 遍历链表"""

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.val
            cur = cur.next

    """Fun5: 头部添加元素"""

    def add(self, val):
        listnode = ListNode(val)
        listnode.next = self._head
        self._head = listnode

    """Fun6: 尾部添加元素"""

    def append(self, val):
        node = ListNode(val)
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    """Fun7: 指定位置插入链表"""

    def insert(self, index, val):
        if index <= 0:
            self.add(val)
        elif index > self.lenght() - 1:
            self.append(val)
        else:
            node = ListNode(val)
            cur = self._head
            for i in range(index - 1):  # 比如index = 3,当前已经在index = 1处，那么需要移动2次
                cur = cur.next
            node.next = cur.next
            cur.next = node

    """Fun8: 删除值为value的结点"""

    def remove(self, val) -> Boolean:
        cur = self._head
        pre = None
        while cur is not None:
            if cur.val == val:
                if not pre:  # 删除的是第一个节点，即head节点
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False

    """Fun9: 判断某一个元素是否存在"""

    def find(self, val):
        return val in self.items()


"""测试单链表操作"""
# Fun1: 初始化链表
singlelinklist = singleLinkList()
# Fun2: 判断链表是否为空
print(singlelinklist.isEmpty())
for i in range(5):
    # Fun6: 尾部添加元素
    singlelinklist.append(i)
# Fun4: 遍历链表
items = singlelinklist.items()
for i in items:
    print(i, end=" ")
print(" ")
# Fun3: 链表长度
print(singlelinklist.lenght())
# Fun5: 头部添加元素
singlelinklist.add(9)
for i in singlelinklist.items():
    print(i, end=" ")
print(" ")
# Fun7: 指定位置插入链表
singlelinklist.insert(2, 8)
for i in singlelinklist.items():
    print(i, end=" ")
print(" ")
# Fun8: 删除值为value的结点
singlelinklist.remove(3)
for i in singlelinklist.items():
    print(i, end=" ")
print(" ")
# Fun9: 判断某一个元素是否存在
print(singlelinklist.find(3))
