"""
平衡二叉树
"""
from tree import *


class AvlTree(object):
    """FUN0 初始化"""

    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    """FUN1 由无序数组创建平衡二叉树 """

    def avl_create(self, arr):
        for i in arr:
            self.avl_insert(i)

    """FUN2 向平衡二叉树添加节点 """

    def avl_insert(self, val):
        node = TreeNode(val)
        if self.node is None:
            self.node = node
            self.node.left = AvlTree()
            self.node.right = AvlTree()
        elif val < self.node.val:
            self.node.left.avl_insert(val)
        else:
            self.node.right.avl_insert(val)
        # 调整使平衡
        self.avl_rebalance()

    """FUN3 将二叉树恢复平衡"""

    def avl_rebalance(self):
        # 计算平衡因子
        self.avl_heights(False)
        self.avl_balance(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance < -1:                       # R
                if self.node.right.balance > 0:         # 如果是RL
                    self.node.right.avl_rotate_right()  # 对RL需要先转化成RR
                    self.avl_heights()
                    self.avl_balance()
                self.avl_rotate_left()                  # RR
                self.avl_heights()
                self.avl_balance()
            if self.balance > 1:                        # L
                if self.node.left.balance < 0:          # 如果是LR
                    self.node.left.avl_rotate_left()    # 对LR需要先转换成LL
                    self.avl_heights()
                    self.avl_balance()
                self.avl_rotate_right()                 # LL
                self.avl_heights()
                self.avl_balance()

    """FUN4 计算每个结点的height"""

    def avl_heights(self, recursive=True):
        if self.node is None:
            self.height = -1
        else:
            if recursive:  # 在插入结点时计算高度，由上到下计算高度； 结点调换位置时，由下到上计算高度
                if self.node.left:
                    self.node.left.avl_heights()
                if self.node.right:
                    self.node.right.avl_heights()
            self.height = 1 + max(self.node.left.height, self.node.right.height)

    """FUN5 计算每个结点的balance"""

    def avl_balance(self, recursive=True):
        if self.node is None:
            self.balance = 0
        else:
            if recursive:
                if self.node.left:
                    self.node.left.avl_balance()
                if self.node.right:
                    self.node.right.avl_balance()
            self.balance = self.node.left.height - self.node.right.height

    """FUN6 左旋"""

    def avl_rotate_left(self):
        new_root = self.node.right.node
        new_sub_left = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_sub_left
        new_root.left.node = old_root

    """FUN7 右旋"""

    def avl_rotate_right(self):
        new_root = self.node.left.node
        new_sub_right = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_sub_right
        new_root.right.node = old_root

    """FUN9 中序遍历平衡二叉树，并打印结果"""

    def avl_inorder(self):
        if self.node is None:
            return
        if self.node.left:
            self.node.left.avl_inorder()
        print("val:{}, height:{}, balance:{}".format(self.node.val, self.height, self.balance))
        if self.node.right:
            self.node.right.avl_inorder()

    """FUN10 打印平衡二叉树图形"""

    def avl_print_graph(self):
        """FUN11 将平衡二叉树转化为普通的二叉树"""
        root = self.acl2Btree()
        # 打印转化后的树
        tree_print_graph(root)

    """FUN11 将平衡二叉树转化为普通的二叉树"""

    def acl2Btree(self):
        if self.node is None:
            return
        root = TreeNode(self.node.val)
        if self.node.left:
            root.left = self.node.left.acl2Btree()
        if self.node.right:
            root.right = self.node.right.acl2Btree()
        return root


arr = [1, 2, 3, 4, 5, 6]
# arr = [3, 4, 2, 1, 6, 5]
# arr = [-10, -3, 0, 5, 9]
"""FUN0 初始化"""
avl = AvlTree()
"""FUN1 由无序数组创建平衡二叉树 """
avl.avl_create(arr)
"""FUN9 中序遍历平衡二叉树"""
avl.avl_inorder()
"""FUN10 打印平衡二叉树图形"""
avl.avl_print_graph()

# 不创建平衡二叉树的类 的情况下

#
# """FUN1 由无序数组创建平衡二叉树 """
# """
# 插入结点
# 检查是否平衡
# 不平衡的话调整成平衡二叉树
# """
#
#
# def avl_create(arr: List[int]):
#     root = TreeNode(arr[0])
#     for i in arr[1:]:
#         avl_add(root, i)
#     return root
#
#
# """FUN2 向平衡二叉树添加节点 """
#
#
# def avl_add(root, i):
#     if root.val > i:
#         if root.left is None:
#             root.left = TreeNode(i)
#         else:
#             avl_add(root.left, i)
#     else:
#         if root.right is None:
#             root.right = TreeNode(i)
#         else:
#             avl_add(root.right, i)
#
#
#
#
#
# # arr = [1, 2, 3, 4, 5, 6]
# arr = [3, 4, 2, 1, 6, 5]
# root = avl_create(arr)
# tree_print_graph(root)
