# Definition for singly-linked list.
from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reversePrint(self, head: ListNode) -> List[int]:
        """
        :type head: ListNode
        :rtype: List[int]
        """
        return self.reversePrint(head.next) + [head.val] if head else []
        # if head:
        #     re = self.reversePrint(head.next) + [head.val]
        #     return re
        # else:
        #     return []

    def reversePrint2(self, head: ListNode) -> List[int]:

        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(2)

s = Solution()
print(s.reversePrint(head))
print(s.reversePrint2(head))
