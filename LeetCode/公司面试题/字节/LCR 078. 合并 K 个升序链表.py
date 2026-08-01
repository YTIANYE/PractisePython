"""
给定一个链表数组，每个链表都已经按升序排列。

请将所有链表合并到一个升序链表中，返回合并后的链表。

 

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

# 我的题解：堆排序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        phead = ListNode()
        p = phead
        nodes = []
        idx = 0
        for node in lists:
            if node:  # 注意判空
                heapq.heappush(nodes, (node.val, idx, node))
                idx += 1    # 注意位置与下方自增位置相同
        while nodes:
            val, _, node = heapq.heappop(nodes)
            p.next = node
            p = node
            if node.next:
                q = node.next
                heapq.heappush(nodes, (q.val, idx, q))  # 注意使用方式
                idx += 1
        return phead.next

# 我的题解：分治递归
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1, list2):
        phead = ListNode()
        pre = phead
        p = list1
        q = list2
        while p or q:
            if not p:
                pre.next = q
                break
            if not q:
                pre.next = p
                break
            if p.val <= q.val:
                pre.next = p
                p = p.next
            else:
                pre.next = q
                q = q.next
            pre = pre.next
        return phead.next

    def mergeLists(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        return self.mergeTwoLists(
            self.mergeLists(lists, left, mid), self.mergeLists(lists, mid + 1, right)
        )

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

