"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 

示例 1：


输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：


输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000
 

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        # 递归
        def rev(new_head, p, q):
            if q.next is None:
                new_head.next = q
            else:
                rev(new_head, p.next, q.next)
            q.next = p 
            p.next = None 
        new_head = ListNode(0, None)
        rev(new_head, head, head.next)
        return new_head.next

        # 迭代
        # phead = ListNode(0, head)
        # p = head
        # q = head.next 
        # while q is not None:
        #     p.next = q.next 
        #     q.next = phead.next 
        #     phead.next = q 
        #     q = p.next 
        # return phead.next 


class Solution_0:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None:
        #     return head 
        # # 递归
        # newhead = self.reverseList(head.next)
        # head.next.next = head 
        # head.next = None 
        # return newhead

        # 迭代
        prehead = None 
        cur = head 
        while cur is not None:
            nex = cur.next 
            cur.next = prehead
            prehead = cur 
            cur = nex 
        return prehead