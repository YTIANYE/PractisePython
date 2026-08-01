"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
 

示例 1：


输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：

输入：head = [], val = 1
输出：[]
示例 3：

输入：head = [7,7,7,7], val = 7
输出：[]
 

提示：

列表中的节点数目在范围 [0, 104] 内
1 <= Node.val <= 50
0 <= val <= 50
"""

# 我的题解：迭代
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        phead = ListNode(0, head)
        p = phead 
        while p.next:
            q = p.next 
            if q.val == val:
                p.next = q.next 
            else:
                p = p.next 
        return phead.next  

# 官方题解：递归
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 基线条件：空链表直接返回
        if head is None:
            return head
        
        # 递归处理下一个节点，接到当前节点后面
        head.next = self.removeElements(head.next, val)
        
        # 当前节点值等于目标值：跳过当前节点，返回下一个节点
        # 否则保留当前节点，直接返回自己
        return head.next if head.val == val else head