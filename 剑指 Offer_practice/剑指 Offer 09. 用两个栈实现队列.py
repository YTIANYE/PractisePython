"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )


示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对appendTail、deleteHead 进行10000次调用
"""


class CQueue1:
    # 我的题解:维护一个队列
    """
    执行用时：880 ms, 在所有 Python3 提交中击败了15.77%的用户
    内存消耗：18.7 MB, 在所有 Python3 提交中击败了38.13%的用户
    """

    def __init__(self):
        self.stackHead = []
        self.stackTail = []

    # 清空一个栈到另一个栈中
    def stack1_to_stack2(self, stack1, stack2):
        while len(stack1) > 0:
            stack2.append(stack1[-1])
            stack1.pop()

    def appendTail(self, value: int) -> None:
        if len(self.stackTail) > 0:
            self.stack1_to_stack2(self.stackTail, self.stackHead)
        self.stackTail.append(value)

    def deleteHead(self) -> int:
        if len(self.stackHead) > 0:
            self.stack1_to_stack2(self.stackHead, self.stackTail)
        if len(self.stackTail) > 0:
            v = self.stackTail.pop()
            return v
        return -1


class CQueue2:
    # 我的题解
    """
    执行用时：1656 ms, 在所有 Python3 提交中击败了5.08%的用户
    内存消耗：18.7 MB, 在所有 Python3 提交中击败了26.09%的用户
    """

    def __init__(self):
        self.stackHead = []
        self.pHead = -1
        self.stackTail = []
        self.pTail = -1

    def stack2stack(self, order: int):
        if order == 0:  # Head -> Tail
            while self.pHead > -1:
                self.pTail += 1
                self.stackTail.append(self.stackHead[-1])
                self.stackHead.pop()
                self.pHead -= 1
        elif order == 1:  # Tail -> Head
            while self.pTail > -1:
                self.pHead += 1
                self.stackHead.append(self.stackTail[-1])
                self.stackTail.pop()
                self.pTail -= 1

    def appendTail(self, value: int) -> None:
        if self.pTail > -1:
            self.stack2stack(1)
        self.pTail += 1
        self.stackTail.append(value)

    def deleteHead(self) -> int:
        if self.pHead > -1:
            self.stack2stack(0)
        if self.pTail > -1:
            value = self.stackTail.pop()
            self.pTail -= 1
            return value
        return -1


"""最优解"""


class CQueue:
    # 我实现的官方题解
    """
    执行用时：340 ms, 在所有 Python3 提交中击败了54.35%的用户
    内存消耗：18.7 MB, 在所有 Python3 提交中击败了24.76%的用户
    """
    def __init__(self):
        self.stack1 = []  # 待插入队列
        self.stack2 = []  # 待删除队列

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if len(self.stack2) > 0 else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()app

if __name__ == "__main__":
    queue = CQueue()
    while True:
        order = input("输入命令(appendTail、deleteHead):")
        if order == "appendTail":
            value = int(input("value = "))
            queue.appendTail(value)
        elif order == "deleteHead":
            value = queue.deleteHead()
            print(value)
        else:
            pass
