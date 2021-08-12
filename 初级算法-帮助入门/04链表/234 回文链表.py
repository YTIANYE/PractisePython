"""
请判断一个链表是否为回文链表。

输入: 1->2->2->1
输出: true

输入: 1->2
输出: false

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

"""
from LinkListPractise import *


class Solution:
    """
    执行用时：820 ms, 在所有 Python3 提交中击败了48.72%的用户
    内存消耗：47.9 MB, 在所有 Python3 提交中击败了45.77%的用户
    """
    # 我的题解
    # O(n) 时间复杂度和 O(n) 空间复杂度
    def isPalindrome1(self, head: ListNode) -> bool:
        stack = []
        cur = head
        while cur is not None:
            stack.append(cur.val)
            cur = cur.next
        return stack == stack[::-1]

    """
    执行用时：1156 ms, 在所有 Python3 提交中击败了5.02%的用户
    内存消耗：140.2 MB, 在所有 Python3 提交中击败了5.03%的用户
    """
    # 官方题解: 递归，    递归消耗极大
    # O(n) 时间复杂度和 O(n) 空间复杂度
    def isPalindrome2(self, head: ListNode) -> bool:
        self.front = head

        def check(cur):
            if cur is not None:
                if not check(cur.next):
                    return False
                if cur.val != self.front.val:
                    return False
                self.front = self.front.next
            return True

        return check(head)

    """
    执行用时：972 ms, 在所有 Python3 提交中击败了13.99%的用户
    内存消耗：47.9 MB, 在所有 Python3 提交中击败了47.98%的用户
    """
    # 官方题解：双指针，快慢指针
    def isPalindrome(self, head: ListNode) -> bool:

        def reserve(head: ListNode) -> ListNode:
            cur = head
            yummy = ListNode(-1)
            while cur is not None:
                node = cur.next
                cur.next = yummy.next
                yummy.next = cur
                cur = node
            return yummy.next

        def findmidpointer(head: ListNode) -> ListNode:
            slow = fast = head
            # 注意检查快指针后面两个结点
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow

        if head is None:
            return True
        first = findmidpointer(head)
        second = reserve(first.next)
        tag = True
        cur = head
        cur2 = second
        while cur is not None and cur2 is not None:
            if cur.val != cur2.val:
                tag = False
            cur = cur.next
            cur2 = cur2.next
        first.next = reserve(second)
        return tag


s = Solution()
l1 = [1, 2, 2, 1, 2]
head = arrToLinkList(l1)
print(s.isPalindrome(head))
