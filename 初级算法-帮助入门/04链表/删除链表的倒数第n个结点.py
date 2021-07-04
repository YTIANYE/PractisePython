"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

输入：head = [1], n = 1
输出：[]

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了90.88%的用户
    内存消耗：15 MB, 在所有 Python3 提交中击败了10.64%的用户
    """

    # 我的题解：双指针
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        pre = head
        cur = head
        # 比如n = 3, 执行4次，
        # cur是pre后面的第4个结点，
        # 当cur == None，pre是倒数第4个结点
        # pre.next 则是要删除的结点
        for i in range(n + 1):
            if cur is None:
                head = head.next
                return head
            cur = cur.next
        while cur is not None:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next
        return head

    # 官方题解双指针，用哑结点更简便
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

    """
    执行用时：44 ms, 在所有 Python3 提交中击败了51.60%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了23.68%的用户
    """

    # 官方题解方法二：栈
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)  # 哑结点，指向头结点的结点
        dummy.next = head
        stack = []
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        for i in range(n):
            stack.pop()
        pre = stack[-1]
        pre.next = pre.next.next
        return dummy.next


# 打印链表
def printLinkList(head: ListNode):
    cur = head
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print("\n")


# 由数组创建链表
def arrToLinkList(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


s = Solution()
arr = [0, 1, 2, 3, 4]
head = arrToLinkList(arr)
printLinkList(head)
# 去除倒数第5个
head = s.removeNthFromEnd(head, 5)
printLinkList(head)
# 去除倒数第1个
head = s.removeNthFromEnd(head, 1)
printLinkList(head)
# 去除倒数第2个
head = s.removeNthFromEnd(head, 2)
printLinkList(head)
