from tree import TreeNode
"""最小深度是从根节点到最近叶子节点的最短路径上的节点数量。"""

# 求最小深度：递归方式
def min_depth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    if root.left is not None or root.right is not None:     # 只要它有一个子节点，就要继续算下去，所以是max
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    return min(self.minDepth(root.left), self.minDepth(root.right)) + 1     # +1 表示返回了自己这一节点的高度
    # 或许 直接 return 1 就可以了，因为左右子节点均为None才执行这一 return 语句


# 求最小深度：iterative迭代方式，层次遍历
def min_height(root):
    if root is None:
        return 0
    height = 0
    level = [root]
    while level:
        height += 1
        new_level = []
        for node in level:
            if node.left is None and node.right is None:
                return height
            if node.left is not None:
                new_level.append(node.left)
            if node.right is not None:
                new_level.append(node.right)
        level = new_level
    return height


# 打印一棵树(先序遍历方式)
def print_tree(root):
    if root is not None:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)


if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(12)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(25)
    tree.left.left.right = TreeNode(100)
    tree.left.right = TreeNode(30)
    tree.right.left = TreeNode(36)

    height = min_height(tree)
    print_tree(tree)
    print("height:", height)

    depth = min_depth(tree)
    print("depth:", depth)
