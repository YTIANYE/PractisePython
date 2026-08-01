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

# 官方题解： 堆排序
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

# 官方题解： 分治递归
from typing import List

# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 合并两个有序链表，对应C++ mergeTwoLists
    def mergeTwoLists(self, a: ListNode, b: ListNode) -> ListNode:
        if not a or not b:
            return a if a else b
        # 虚拟头节点，对应C++局部栈变量head
        head = ListNode()
        tail = head
        a_ptr, b_ptr = a, b
        
        while a_ptr and b_ptr:
            if a_ptr.val < b_ptr.val:
                tail.next = a_ptr
                a_ptr = a_ptr.next
            else:
                tail.next = b_ptr
                b_ptr = b_ptr.next
            tail = tail.next
        # 拼接剩余链表
        tail.next = a_ptr if a_ptr else b_ptr
        return head.next

    # 分治递归：合并 [l, r] 区间内所有链表
    def merge(self, lists: List[ListNode], l: int, r: int) -> ListNode:
        if l == r:
            return lists[l]
        if l > r:
            return None
        # 等价 (l + r) // 2，C++ (l+r)>>1 整数右移除2
        mid = (l + r) // 2
        left = self.merge(lists, l, mid)
        right = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(left, right)

    # 主函数入口
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)


# 我的题解  分治递归
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