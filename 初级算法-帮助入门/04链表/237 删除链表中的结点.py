"""
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。

 示例 1：

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

提示：

链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    """
    注意这题要求传入的是要删除的结点，
    要用下一个结点的值覆盖该节点，
    并将该节点的下一个结点删除
    """
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


