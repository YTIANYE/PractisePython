"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，
每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class LinkList:
    def __init__(self, head):
        first = Node(0, None, None)  # 无意义的头结点
        p = first
        self.nodes = []
        for i in range(len(head)):
            node = Node(head[i][0], None, None)
            p.next = node
            p = node
            self.nodes.append(node)
        p = first.next
        for i in range(len(head)):
            if head[i][1] is None:
                p.random = None
            else:
                p.random = self.nodes[head[i][1]]
            p = p.next
        self.list = first.next

    def printList(self):
        nodes = self.nodes
        p = self.list
        result = []
        while p:
            out = [p.val]
            if p.random:
                for i in range(len(nodes)):
                    if nodes[i] == p.random:
                        out.append(i)
            else:
                out.append(None)
            p = p.next
            result.append(out)
        print(result)


class Solution:
    # 我的题解：先根据next建立链表，再赋值random指针
    """
    执行用时：60 ms, 在所有 Python3 提交中击败了5.04%的用户
    内存消耗：15.7 MB, 在所有 Python3 提交中击败了36.22%的用户
    """

    def copyRandomList1(self, head: 'Node') -> 'Node':

        copy = Node(0, None, None)
        q = copy
        p = head
        pnodes = []
        qnodes = []

        # 返回pnodes中某个node的索引
        def index(pnodes, random):
            for i in range(len(pnodes)):
                if random == pnodes[i]:
                    return i
            return None

        # 沿着next创建链表，并记录qnode
        while p:
            pnodes.append(p)
            node = Node(p.val, None, None)
            q.next = node
            qnodes.append(node)
            q = q.next
            p = p.next

        # 赋值random
        p = head
        q = copy.next
        while p:
            if p.random:
                num = index(pnodes, p.random)
                q.random = qnodes[num]
            else:
                q.random = None
            p = p.next
            q = q.next
        self.qNodes(qnodes)
        return copy.next

    def qNodes(self, qnodes):
        self.qnodes = qnodes

    # 我的题解改进：新旧结点对应字典 替代 两个nodes数组
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了71.17%的用户
    内存消耗：15.9 MB, 在所有 Python3 提交中击败了12.66%的用户
    """

    def copyRandomList(self, head: 'Node') -> 'Node':
        nodes = {}  # 新旧结点对应字典
        p = head
        new_head = Node(0, None, None)
        q = new_head
        # 直接next下去复制全部节点
        while p:
            node = Node(p.val, None, None)
            q.next = node
            q = q.next
            nodes[p] = q
            p = p.next
        # 连接random
        p = head
        q = new_head.next
        while p:
            if p.random is None:
                q.random = None
            else:
                q.random = nodes[p.random]
            p = p.next
            q = q.next
        return new_head.next

    # 我实现的 官方题解：递归建立
    def copyRandomList3(self, head: 'Node') -> 'Node':
        nodes = {}  # 记录新旧结点的对应关系，用于建立random

        def deep(head) -> 'Node':
            if head is None:
                return None
            if head not in nodes.keys():
                new_node = Node(head.val, None, None)
                nodes[head] = new_node
                new_node.next = deep(head.next)
                new_node.random = deep(head.random)
            else:  # 只有deep(head.random)时执行
                return nodes[head]
            return new_node

        return deep(head)

    # 我实现的 官方题解：迭代 + 结点拆分
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了45.35%的用户
    内存消耗15.6 MB, 在所有 Python3 提交中击败了65.42%的用户
    """

    def copyRandomList4(self, head: 'Node') -> 'Node':
        if head is None:  # head = []     需要特殊判断
            return None
        # 每个结点之后赋值一个同样val的结点
        p = head
        while p:
            p.next = Node(p.val, p.next, None)
            p = p.next.next
        # random连接
        p = head
        while p:
            if p.random is None:  # 注意None特殊判断
                p.next.random = None
            else:
                p.next.random = p.random.next
            p = p.next.next
        # 拆分
        new_head = head.next
        p = head
        q = head.next
        while p:
            p.next = p.next.next
            if q.next is not None:  # 末尾特殊判断一下
                q.next = q.next.next
            p = p.next
            q = q.next
        return new_head

    # 我的题解： 改进 迭代 + 拆分
    # 无法解决random指向的结点出现环的情况     # head = [[-1, 4], [8, 3], [7, None], [-3, None], [4, 0]]
    def copyRandomList5(self, head: 'Node') -> 'Node':
        def hascopy(head):
            if head.next and head.val == head.next.val \
                    and ((head.random is None and head.next.random is None)
                         or head.random and head.random.next == head.next.random):
                return True  # 有复制节点了
            return False

        def creat(head):
            if head is None:
                return None
            if not hascopy(head):  # a的复制结点还未创建，或者是链表末端结点
                if head.random == head:  # random指向自己需要特殊判断一下，避免进入死循环
                    head.next = Node(head.val, head.next, None)
                    head.next.random = head.next
                else:
                    head.next = Node(head.val, head.next, creat(head.random))
            return head.next

        # 如果复制结点还未创建，或者结点a是链表最后一个结点
        # 创建一个与当前结点a的val一样的复制结点b作为当前结点的next
        # 创建b时，递归调用create()创建b.random

        if head is None:  # head = []     需要特殊判断
            return None
        """第一次遍历，创建所需的结点"""
        p = head
        while p:
            p.next = creat(p)
            p = p.next.next

        """第二次遍历：拆分"""
        new_head = head.next
        p = head
        q = head.next
        while p:
            p.next = p.next.next
            if q.next is not None:  # 末尾特殊判断一下
                q.next = q.next.next
            p = p.next
            q = q.next
        return new_head


s = Solution()
# head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# head = [[1, 1], [2, 1]]
# head = [[3, None], [3, 0], [3, None]]
# head = []
head = [[-1, 4], [8, 3], [7, None], [-3, None], [4, 0]]
linklist = LinkList(head)
print("原链表")
linklist.printList()  # 输出原链表

# 复制链表
copy = s.copyRandomList(linklist.list)
linklist.list = copy

# # 方法一测试
# linklist.nodes = s.qnodes
# linklist.printList()

# 其他方法测试
p = linklist.list
result = []
while p:
    r = [p.val]
    if p.random:
        r.append(p.random.val)
    else:
        r.append(None)
    result.append(r)
    p = p.next
print(result)  # 简化打印，random直接打印了指向结点的val, 而不是链表中的序号
