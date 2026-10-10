from tree import *

# arr = [0, 1, 2, null, 4, 5, 6, null, null, 9]
arr = [0, 1, 2, 3, 4, 5, 6]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
# arr = ['a', 'b', 'c', 'd', null, 'f', 'g', 'h', 'i', null, null, 'l', 'm', 'n', 'o', 'p', 'q', 'r']
print('\n' + "FUN1 由数组创建一棵树")
root = tree_create(arr, 0)

# print('\n' + "FUN2 遍历一棵树: preorder inorder postorder level")
# tree_traversing(root, traversal="level")  # 默认preorder
# print()

# print('\n' + "FUN2.1 层次遍历一棵树，以数组的形式返回遍历结果")
# print(tree_level(root))

# print('\n' + "FUN2.2 层次遍历一棵树，以数组的形式返回遍历结果， 包含空结点null")
# print(tree_level2(root))

# print('\n' + "FUN2.3 层次遍历一棵树，以数组的形式返回遍历结果(完全二叉树，空结点-1补全), 用于绘制图形")
# print(tree_level_complete_binary_tree(root))

print('\n' + "FUN3 一棵树的最大深度")
print("二叉树的最大深度：", tree_depth(root))

print('\n' + "FUN4 打印一棵二叉树图形")
tree_print_graph(root)

# print('\n' + "FUN5 添加结点: 层序遍历，保持二叉树一直是完全二叉树")
# for i in [7, 8, 9]:
#     tree_add(root, i)
# tree_print_graph(root)
