"""
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder =     [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

限制：
0 <= 节点个数 <= 5000

"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self, preorder, inorder) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) != 0:
            father = preorder[0]
            node = TreeNode(father)
            for i in range(len(inorder)):
                if inorder[i] == father:
                    if i != 0:
                        node.left = self.buildTree(preorder[1:i+1], inorder[0:i])
                    if len(inorder) - 1 - i != 0:
                        node.right = self.buildTree(preorder[i+1:], inorder[i+1: ])
                    break
            return node

    # 题解方法如下
    def buildTree2(self, preorder, inorder) -> TreeNode:
        # root 是preorder中father的索引， left 和 right 是 inorder中的索引
        def recur(root, left, right):
            if left > right: return  # 递归终止
            node = TreeNode(preorder[root])  # 建立根节点
            # i 表示inorder中father的位置
            i = dic[preorder[root]]  # 划分根节点、左子树、右子树
            node.left = recur(root + 1, left, i - 1)  # 开启左子树递归
            # i - left 表示左子树的长度
            node.right = recur(i - left + root + 1, i + 1, right)  # 开启右子树递归
            return node  # 回溯返回根节点

        dic, preorder = {}, preorder
        # 减少查询时间
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s.buildTree(preorder, inorder)
