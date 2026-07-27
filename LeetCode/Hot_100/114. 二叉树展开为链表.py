"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [0]
输出：[0]
 

提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100
 

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 我的题解
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """

#         if root is None:
#             return 
#         if root.left is None:
#             self.flatten(root.right)
#         else:
#             node = self.find_last(root.left)
#             node.right = root.right 
#             root.right = root.left 
#             root.left = None 
#             self.flatten(root.right)

    
#     # 寻找先序遍历最后一个结点
#     def find_last(self, root):
#         if root.right:
#             return self.find_last(root.right)
#         if root.left:
#             return self.find_last(root.left)
#         return root 
        

# 官方题解
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
"""
我的题解找到是左子树先序遍历的最后一个结点，官方题解中找的是左子树最后边的结点，在左子树是这种情况下，
    a
b 
我找的是b，官方找的是a, 都不影响，后续处理到a结点的时候，官方题解中还会在处理一次a的右子树，而我的题解就免了这一步了。
"""