"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""
from LinkListPractise import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 我的题解: 头插法
    """
    执行用时：44 ms, 在所有 Python3 提交中击败了12.84%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了76.64%的用户
    """

    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node = ListNode(0)
        node.next = head
        p = head.next
        while p:
            head.next = p.next
            p.next = node.next
            node.next = p
            p = head.next
        return node.next

    # 我实现的官方题解：依次反转指针
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了32.69%的用户
    内存消耗：15.5 MB, 在所有 Python3 提交中击败了64.72%的用户
    """

    def reverseList2(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    # 我实现的官方题解：依次反转指针  迭代版本
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了94.03%的用户
    内存消耗：19.6 MB, 在所有 Python3 提交中击败了12.74%的用户
    """

    def reverseList3(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = self.reverseList(head.next)  # 注意调用方法
        head.next.next = head
        head.next = None  # 注意原头结点赋值为None
        return node  # 注意返回结点

    # 精选题解：迭代
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回


if __name__ == "__main__":

    test = [[1, 2, 3, 4, 5],
            [],
            [1]]
    for arr in test:
        head = arrToLinkList(arr)
        s = Solution()
        reverse = s.reverseList(head)
        printLinkList(reverse)
