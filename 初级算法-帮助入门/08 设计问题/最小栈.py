"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) —— 将元素 x 推入栈中。
pop()—— 删除栈顶的元素。
top()—— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。
"""


class MinStack:

    # 我的题解
    """
    执行用时：440 ms, 在所有 Python3 提交中击败了18.70%的用户
    内存消耗：18.1 MB, 在所有 Python3 提交中击败了30.11%的用户
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return min(self.stack)

    # 官方题解：辅助栈  设置一个辅助栈存储栈中每个元素对应的包含之前所有元素中的最小值，辅助栈与栈同步增删

if __name__ == "__main__":
    string = input("请输入命令（MinStack）")
    if string == "MinStack":
        minStack = MinStack()
    while True:
        string = input("请输入命令（push、pop、getMin、top）")
        if string == "push":
            minStack.push(int(input("请输入value")))
        elif string == "pop":
            minStack.pop()
        elif string == "getMin":
            print(minStack.getMin())
        elif string == "top":
            print(minStack.top())

