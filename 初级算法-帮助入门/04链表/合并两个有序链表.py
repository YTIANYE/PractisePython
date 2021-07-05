"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

输入：l1 = [], l2 = []
输出：[]

输入：l1 = [], l2 = [0]
输出：[0]
"""
from typing import List
from LinkListPractise import *


class Solution:
    """
    执行用时：52 ms, 在所有 Python3 提交中击败了19.43%的用户
    内存消耗：14.8 MB, 在所有 Python3 提交中击败了83.86%的用户
    """
    # 我的题解: 迭代
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
            node.next = None
            cur.next = node
            cur = cur.next
        cur.next = l1 if l1 else l2
        return head.next

    # 官方题解： 递归
    def mergeTwoLists(self, l1: ListNode, l2:ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


s = Solution()
l1 = [1, 2, 4]
l2 = [1, 3, 4]
# l1 = []
# l2 = []
# l1 = []
# l2 = [0]
list1 = arrToLinkList(l1)
list2 = arrToLinkList(l2)
head = s.mergeTwoLists(list1, list2)
printLinkList(head)
