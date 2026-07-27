"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]
 

提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 我的题解
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if len(preorder) == 0:
#             return None 

#         root = TreeNode(preorder[0])
#         mid = 0 
#         if len(preorder) == 1:
#             return root 

#         # 优化点：可以用哈希代替 
#         for i in range(len(inorder)):
#             if inorder[i] == preorder[0]:
#                 mid = i 
#                 break 
#         # 优化点：新增自定义函数递归，传list下标
#         if mid == 0:
#             lp = []
#             rp = preorder[mid+1:]
#             li = []
#             ri = inorder[mid+1:]
#         elif mid == len(inorder) - 1:
#             lp = preorder[1:mid+1]
#             rp = []
#             li = inorder[:mid]
#             ri = []
#         else:
#             lp = preorder[1:mid+1]
#             rp = preorder[mid+1:]
#             li = inorder[:mid]
#             ri = inorder[mid+1:]
#         root.left = self.buildTree(lp, li)
#         root.right = self.buildTree(rp, ri)
#         return root 


# # 官方题解
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
#             if preorder_left > preorder_right:
#                 return None
            
#             # 前序遍历中的第一个节点就是根节点
#             preorder_root = preorder_left
#             # 在中序遍历中定位根节点
#             inorder_root = index[preorder[preorder_root]]
            
#             # 先把根节点建立出来
#             root = TreeNode(preorder[preorder_root])
#             # 得到左子树中的节点数目
#             size_left_subtree = inorder_root - inorder_left
#             # 递归地构造左子树，并连接到根节点
#             # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
#             root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
#             # 递归地构造右子树，并连接到根节点
#             # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
#             root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
#             return root
        
#         n = len(preorder)
#         # 构造哈希映射，帮助我们快速定位根节点
#         index = {element: i for i, element in enumerate(inorder)}
#         return myBuildTree(0, n - 1, 0, n - 1)

# 我实现的官方题解
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hash = {v: i for i, v in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return 
            val = preorder[pre_left]
            node = TreeNode(val)
            index = hash[val]
            len_left = index - in_left
            node.left = build(pre_left + 1, pre_left + len_left, in_left, index - 1)
            node.right = build(pre_left + len_left + 1, pre_right, index + 1, in_right)
            return node 
        
        return build(0, len(preorder)-1, 0, len(inorder) - 1)