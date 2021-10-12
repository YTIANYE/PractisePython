"""
用于为LeetCode函数测试
提供链表的基本数据结构和基本操作
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 打印链表
def printLinkList(head: ListNode):
    cur = head
    while cur is not None:
        print(cur.val, end=" ")
        cur = cur.next
    print("\n")


# 由数组创建链表
def arrToLinkList(arr: List[int]) -> ListNode:
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


# 求链表长度
def lenghtOfLinkList(head: ListNode) -> int:
    cur = head
    count = 0
    while cur is not None:
        count += 1
        cur = cur.next
    return count
