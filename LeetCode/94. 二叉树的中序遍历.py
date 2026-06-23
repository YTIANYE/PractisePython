"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
 

提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
 

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# class Solution_0:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.list = []
#         def inorder(node):
#             if node is None:
#                 return None
#             inorder(node.left)
#             self.list.append(node.val)
#             inorder(node.right)
#         inorder(root)
#         return self.list


# # 迭代
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#         stack = []
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
#         return res

# Morris 中序遍历
"""
Morris 遍历算法整体步骤如下（假设当前遍历到的节点为 x）：

如果 x 无左孩子，先将 x 的值加入答案数组，再访问 x 的右孩子，即 x=x.right。
如果 x 有左孩子，则找到 x 左子树上最右的节点（即左子树中序遍历的最后一个节点，x 在中序遍历中的前驱节点），我们记为 predecessor。根据 predecessor 的右孩子是否为空，进行如下操作。
如果 predecessor 的右孩子为空，则将其右孩子指向 x，然后访问 x 的左孩子，即 x=x.left。
如果 predecessor 的右孩子不为空，则此时其右孩子指向 x，说明我们已经遍历完 x 的左子树，我们将 predecessor 的右孩子置空，将 x 的值加入答案数组，然后访问 x 的右孩子，即 x=x.right。

"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        predecessor = None 
        while (root):
            if root.left is None:
                res.append(root.val)
                root = root.right 
            else:
                predecessor = root.left 
                while (predecessor.right and predecessor.right != root):
                    predecessor = predecessor.right 
                if predecessor.right is None:
                    predecessor.right = root 
                    root = root.left 
                else :
                    res.append(root.val)
                    predecessor.right = None 
                    root = root.right 
        return res 


            