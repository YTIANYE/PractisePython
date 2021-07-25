"""
平衡二叉树
"""
from tree import *

"""FUN1 由无序数组创建平衡二叉树 """
"""
插入结点
检查是否平衡
不平衡的话调整成平衡二叉树
"""


def avl_create(arr: List[int]):
    root = TreeNode(arr[0])
    for i in arr[1:]:
        avl_add(root, i)
    return root


"""FUN2 向平衡二叉树添加节点 """


def avl_add(root, i):
    if root.val > i:
        if root.left is None:
            root.left = TreeNode(i)
        else:
            avl_add(root.left, i)
    else:
        if root.right is None:
            root.right = TreeNode(i)
        else:
            avl_add(root.right, i)


"""FUN3 将二叉树恢复平衡"""
def avl_balance(root):



# arr = [1, 2, 3, 4, 5, 6]
arr = [3, 4, 2, 1, 6, 5]
root = avl_create(arr)
tree_print_graph(root)
