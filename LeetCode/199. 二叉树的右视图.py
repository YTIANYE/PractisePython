"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

示例 1：

输入：root = [1,2,3,null,5,null,4]

输出：[1,3,4]

解释：



示例 2：

输入：root = [1,2,3,4,null,null,null,5]

输出：[1,3,4,5]

解释：



示例 3：

输入：root = [1,null,3]

输出：[1,3]

示例 4：

输入：root = []

输出：[]

 

提示:

二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def level(root):
            if root is None:
                return 
            # que = [root]
            que = deque([root])
            while que:
                res.append(que[-1].val)
                q = que 
                # que = []
                que = deque([])
                while q:
                    # node = q.pop(0)
                    node = q.popleft()
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
        
        level(root)
        return res 

"""
注释
deque 数据类型来自于collections 模块，支持从头和尾部的常数时间 append/pop 操作。若使用 Python 的 list，通过 list.pop(0) 去除头部会消耗 O(n) 的时间。

"""