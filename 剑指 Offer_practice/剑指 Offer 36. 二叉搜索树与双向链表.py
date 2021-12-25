# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
#
# 我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。
# 对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
#
# “head” 表示指向链表中有最小元素的节点。
#
# 特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
#


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 我的题解:中序遍历后 修改指针指向
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了68.74%的用户
    内存消耗：16.1 MB, 在所有 Python3 提交中击败了10.56%的用户
    """

    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if root is None:  # 特殊情况
            return None

        nodes = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root)
            inorder(root.right)

        inorder(root)

        for i, node in enumerate(nodes):
            if i == 0:
                node.left = nodes[-1]
                if len(nodes) == 1:  # 特殊情况，只有一个结点
                    node.right = node
                else:
                    node.right = nodes[i + 1]
            elif i == len(nodes) - 1:
                node.left = nodes[i - 1]
                node.right = nodes[0]
            else:
                node.left = nodes[i - 1]
                node.right = nodes[i + 1]

        return nodes[0]

    # 我的题解：中序遍历过程中 修改指针指向

    """
    执行用时：36 ms, 在所有 Python3 提交中击败了68.72%的用户
    内存消耗：16 MB, 在所有 Python3 提交中击败了57.18%的用户
    """

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return

        self.pre = None

        def inorder(cur) -> 'Node':
            if not cur:
                return
            inorder(cur.left)

            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:  # 记录头结点
                self.head = cur

            self.pre = cur
            inorder(cur.right)

        inorder(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head
