"""
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 我的题解：迭代
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        phead = ListNode()
        pre = phead 
        temp = 0 
        p1, p2 = l1, l2
        while p1 or p2 or temp != 0:    # 注意处理最后的进位
            val1, val2 = 0, 0
            if p1:
                val1 = p1.val 
                p1 = p1.next 
            if p2:
                val2 = p2.val 
                p2 = p2.next
            val = (val1 + val2 + temp) % 10
            temp = (val1 + val2 + temp) // 10
            pre.next = ListNode(val)
            pre = pre.next 
        return phead.next 
            
            


        
"""
进阶问题中，输入的两个链表都是正向存放数字的位数的，因此链表中数位的顺序与我们做加法的顺序是相反的。

为了反向处理所有数位，我们可以使用栈：把所有数字压入栈中，再依次取出相加。计算过程中需要注意进位的情况。
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        ans = None
        carry = 0
        while s1 or s2 or carry != 0:
            a = 0 if not s1 else s1.pop()
            b = 0 if not s2 else s2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans
