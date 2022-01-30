from typing import List

from pyasn1.compat.octets import null

"""二叉树数据结构"""


class TreeNode:
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None


"""FUN1 由数组 创建一棵树"""


def tree_create(arr, index: int):
    tnode = None
    if index < len(arr):
        if arr[index] == null:
            return
        tnode = TreeNode(arr[index])
        tnode.left = tree_create(arr, index * 2 + 1)
        tnode.right = tree_create(arr, index * 2 + 2)
    return tnode


"""FUN2 遍历一棵树: 先序 中序 后序 层次"""


def tree_traversing(root, traversal="preorder"):
    if root is None:
        return
    # 先序遍历 preorder traversal
    if traversal == "preorder":
        print(root.val, end=" ")
        tree_traversing(root.left, traversal)
        tree_traversing(root.right, traversal)

    # 中序遍历 inorder traversal
    elif traversal == "inorder":
        tree_traversing(root.left, traversal)
        print(root.val, end=" ")
        tree_traversing(root.right, traversal)

    # 后序遍历 postorder traversal
    elif traversal == "postorder":
        tree_traversing(root.left, traversal)
        tree_traversing(root.right, traversal)
        print(root.val, end=" ")

    # 层次遍历 level traversal
    elif traversal == "level":
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)  # 注意队列：pop列头
            print(node.val, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    else:
        pass


"""FUN2.1 层次遍历一棵树，以数组的形式返回遍历结果， 不包含空结点"""


def tree_level(root):
    if root is None:
        return
    tree = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        tree.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return tree


"""FUN2.2 层次遍历一棵树，以数组的形式返回遍历结果， 包含空结点"""


def tree_level2(root):
    tree = []
    if root is None:
        tree.append("null")
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == -1:
            tree.append("null")
            continue
        tree.append(node.val)
        if node.left:
            queue.append(node.left)
        else:
            queue.append(TreeNode(-1))
        if node.right:
            queue.append(node.right)
        else:
            queue.append(TreeNode(-1))
    return tree


"""FUN2.3 层次遍历一棵树，以数组的形式返回遍历结果(与原树高度相同的完全二叉树，空结点-1补全), 用于绘制图形"""


def tree_level_complete_binary_tree(root):
    if root is None:
        return
    depth = tree_depth(root)
    tree_graph = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        tree_graph.append(node.val)
        if node.left:
            queue.append(node.left)
        else:
            queue.append(TreeNode())
        if node.right:
            queue.append(node.right)
        else:
            queue.append(TreeNode())
        tag = True  # 全是null
        for q in queue:
            if q.val != -1:
                tag = False
        if tag:  # 全是null
            break
    for i in range(len(tree_graph), 2 ** depth - 1):
        tree_graph.append(-1)
    return tree_graph


"""FUN3 求一棵树的最大深度"""


def tree_depth(root) -> int:
    # if root is None:
    #     return 0
    # else:
    #     return max(tree_depth(root.left), tree_depth(root.right)) + 1
    return 0 if root is None else max(tree_depth(root.left), tree_depth(root.right)) + 1


"""FUN4 打印一棵二叉树图形"""


def tree_print_graph(root):
    depth = tree_depth(root)
    tree_graph = tree_level_complete_binary_tree(root)
    # print(tree_graph)
    nodes_val = [[] for i in range(depth)]  # 记录每一层的结点
    graph = ["" for i in range(depth)]
    # 排列好结点的位置
    for i in range(depth):
        nodes_val[i] = tree_graph[2 ** i - 1: 2 ** (i + 1) - 1]
        # print(nodes_val)
        for j in range(len(nodes_val[i])):
            if nodes_val[i][j] == -1:
                nodes_val[i][j] = " "
            graph[i] += str(nodes_val[i][j]) + (" " * (2 ** (depth - i + 1) - 1))  # 添加结点之间的间隔,最底层间隔3个“ ”
            # print(graph[i])
        graph[i] = (" " * ((2 ** (depth - i)) - 2)) + graph[i]  # 错开位置,构成树的形状，
        # print(graph[i])
    # print("###################################################################")
    for s in graph:
        print(s)


"""FUN5 添加结点: 层序遍历，保持二叉树一直是完全二叉树"""


def tree_add(root, val):
    if root is None:
        return TreeNode(val)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None:
            new = TreeNode(val)
            node.left = new
            return
        else:
            queue.append(node.left)
        if node.right is None:
            new = TreeNode(val)
            node.right = new
            return
        else:
            queue.append(node.right)

