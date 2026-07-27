"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 

进阶：你是否可以使用 O(1) 空间解决此题？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        jihe = set()
        p = head 
        while p is not None:
            if p in jihe:
                return p 
            jihe.add(p)
            p = p.next
        return None 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return 
        fast, slow = head.next, head 
        while fast != slow:
            slow = slow.next 
            if fast.next is None or fast.next.next is None:
                return
            fast = fast.next.next 
        # a是入环前步数， b 是slow入环后步数，c是一环步数
        # (a + b ) * 2 = a + b + c
        # c = a + b 
        # slow走完一环剩余的步数 c - b ，即与入环前步数 a相等
        # 1 2
        # 2 4
        # 3 3
        # 1 4
        # 2 2
        print(fast.val)
        p = head 
        q = slow.next 
        print(p.val, q.val)
        while p != q:
            p = p.next 
            q = q.next 
        return p
