from tree import *
import collections


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize1(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        if root is None:
            tree.append("null")
            return
        queue = [root]
        while queue:
            tag = True  # 全是 -1
            for q in queue:
                if q.val != 65535:
                    tag = False
            if tag:
                break

            que = queue
            queue = []
            while que:
                node = que.pop(0)
                if node.val == 65535:
                    tree.append("null")
                else:
                    tree.append(node.val)

                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(TreeNode(65535))
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(TreeNode(65535))
        return tree

    # dfs  超时
    def deserialize1(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        def dfs(index: int):
            if data[index] == "null":
                return None
            node = TreeNode(data[index])
            if index * 2 + 1 < len(data):
                node.left = dfs(index * 2 + 1)
            if index * 2 + 2 < len(data):
                node.right = dfs(index * 2 + 2)
            return node

        return dfs(0)

    # 执行用时：116ms, 在所有Python3提交中击败了50.04 %的用户
    # 内存消耗：20.4MB, 在所有Python3提交中击败了37.20 %的用户

    # 由树建立数组
    def serialize(self, root):
        if not root:
            return
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()  # queue 是可能存在 None 的
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        return res

    # 由数组建立树
    def deserialize(self, data):
        if not data:
            return

        i = 1
        root = TreeNode(data[0])
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if data[i] != "null":
                node.left = TreeNode(data[i])
                queue.append(node.left)
            i += 1
            if data[i] != "null":
                node.right = TreeNode(data[i])
                queue.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    # arr = [0, 1, 2, null, 4, 5, 6, null, null, 9]
    # arr = [-1, 0, 1]
    # root = tree_create(arr, 0)
    # tree_print_graph(root)
    #
    # codec = Codec()
    # res = codec.serialize(root)
    # print(res)
    #
    # root1 = tree_create(res, 0)
    # tree_print_graph(root1)
    #
    # root2 = codec.deserialize(res)
    # tree_print_graph(root2)

    arr = [0, 1, 2, null, 4, 5, 6, null, null, 9]
    root = tree_create(arr, 0)
    tree_print_graph(root)

    codec = Codec()
    res = codec.serialize(root)
    print("res", res)
    root1 = codec.deserialize(res)
    tree_print_graph(root1)
