"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

输入：head = []
输出：[]

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""

from LinkListPractise import *


class Solution:
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了20.33%的用户
    内存消耗：15.6 MB, 在所有 Python3 提交中击败了43.16%的用户
    """

    # 我的题解：头插法，迭代
    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            yummy = ListNode(0)
            yummy.next = head
            pre = head
            cur = head.next
            while cur is not None:
                pre.next = cur.next
                cur.next = yummy.next
                yummy.next = cur
                cur = pre.next
        return yummy.next

    """
    执行用时：52 ms, 在所有 Python3 提交中击败了20.33%的用户
    内存消耗：19.6 MB, 在所有 Python3 提交中击败了16.57%的用户
    """

    # 我的题解：头插法： 其实不是递归，还是迭代
    def reverseList2(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            return self.recursion(head, head)

    def recursion(self, head: ListNode, pre: ListNode) -> ListNode:
        if pre.next is None:
            return head
        else:
            cur = pre.next
            pre.next = cur.next
            cur.next = head
            head = cur
            return self.recursion(head, pre)

    # 官方题解：递归
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        newNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newNode


s = Solution()
arr = [1, 2, 3, 4]
head = arrToLinkList(arr)
printLinkList(head)
printLinkList(s.reverseList(head))
