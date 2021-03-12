"""

以下代码用于实现最小公倍数算法：


"""

num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
min = min(num1, num2)
beishu = 1

for i in range(min, 1, -1):
    if (num1 % i == 0) and (num2 % i == 0):
        # {}中不表明阿拉伯数字，按默认顺序
        print("{}和{}的最小公倍数是{}".format(num1, num2, int(num1 * num2 / i)))
        break
        pass
    pass


