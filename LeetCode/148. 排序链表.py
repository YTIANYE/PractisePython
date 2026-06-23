"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
 

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findMid(head):
            if head.next is None:
                return head 
            p = head 
            q = head.next 
            # 1 2 3 4  ,2 
            # 1 2 3 4 5 ,3
            while q is not None:
                q = q.next 
                if q is not None:
                    q = q.next 
                else:
                    return p
                p = p.next 
            return p 

        def merge(h1, h2):
            p = h1 
            q = h2 
            phead = ListNode(0, None)
            pre = phead
            while p is not None and q is not None:
                if p.val < q.val:
                    pre.next = p 
                    p = p.next 
                else:
                    pre.next = q 
                    q = q.next 
                pre = pre.next 
                # print(pre.next)
            if p is not None:
                pre.next = p 
            if q is not None:
                pre.next = q 
            return phead.next 
        
        if head is None or head.next is None:   # 注意返回条件
            return head
        mid = findMid(head)
        # print("mid.val:", mid.val)    # print太多会超时
        t = mid.next 
        mid.next = None 
        return merge(self.sortList(head), self.sortList(t))


                    

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(h1,h2):
            p, q = h1, h2 
            phead = ListNode(0, None)
            pre = phead 
            while p is not None and q is not None:
                if p.val < q.val:
                    pre.next = p 
                    p = p.next 
                else:
                    pre.next = q 
                    q = q.next 
                pre = pre.next 
            if p is not None:
                pre.next = p 
            if q is not None:
                pre.next = q 
            # 日志
            # t = phead.next 
            # nums = []
            # while t is not None:
            #     nums.append(t.val)
            # print(nums)
            return phead.next
        
        if head is None or head.next is None:
            return head 
        length = 0 
        p = head 
        while p is not None:
            p = p.next 
            length += 1 
        # print(length)
        l = 1   
        phead = ListNode(0, head)
        while l < length:   # 注意不包含等于，最后一次已经有序
            # print("l:", l)
            pre = phead 
            curr = phead.next 
            while curr:
                h1 = curr
                for i in range(1, l):   #注意起始条件
                    if curr.next:       # 注意判断条件
                        curr = curr.next
                    else:
                        break
                h2 = curr.next  
                curr.next = None 
                curr = h2
                for i in range(1, l):   # 注意起始条件
                    if curr and curr.next:  # 注意判断条件
                        curr = curr.next
                    else:
                        break
                t = None
                if curr:
                    t = curr.next 
                    curr.next = None 
                pre.next = merge(h1, h2)
                while pre.next:
                    pre = pre.next 
                curr = t
            l *= 2
        return phead.next 


            
                
            




        

