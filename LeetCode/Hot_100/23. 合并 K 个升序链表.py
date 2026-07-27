"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""

# 我的题解
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeList(list1, list2):
            phead = ListNode(0, None)
            head = phead
            p, q = list1, list2  # 注意取第一个节点
            while p and q:
                if p.val <= q.val:
                    head.next = p
                    p = p.next
                else:
                    head.next = q
                    q = q.next
                head = head.next
            # while p is not None:
            #     head.next = p
            #     p = p.next
            #     head = head.next
            # while q is not None:
            #     head.next = q
            #     q = q.next
            #     head = head.next
            head.next = p if p else q
            return phead.next

        l = len(lists)
        if l == 0:
            return None  # 注意不是[]
        if l == 1:
            return lists[0]
        mid = l // 2
        return mergeList(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))  # 注意最后返回合并的过程

# 官方题解
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []
        idx = 0  # 唯一标识，避免节点相等时比较ListNode
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, idx, node))
                idx += 1
        
        dummy = ListNode()
        tail = dummy
        while heap:
            val, _, ptr = heapq.heappop(heap)
            tail.next = ptr
            tail = tail.next
            if ptr.next:
                heapq.heappush(heap, (ptr.next.val, idx, ptr.next))
                idx += 1
        return dummy.next