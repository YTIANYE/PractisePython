"""测试Python"""
import random


class test:

    # Python 三元运算符的替代实现
    def test3operator(self):
        a, b = 5, 2
        maxnum = a if a > b else b
        print(maxnum)

    # 测试随机合成color [2: ] 三位中截取最后一个数字
    def testColor(self):
        color11 = str("%03d" % random.randint(0, 255))
        color1 = color11[2:]
        color = '#' + str("%03d" % random.randint(0, 255))[2:] + str("%03d" % random.randint(0, 255))[2:] + str(
            "%03d" % random.randint(0, 255))[2:]
        print(color)

        c = "137"
        c2 = c[2:]
        print(c2)

    def numtrans(self):
        print(1 / 3)  # 0.3333333333333333
        print(int(1 / 3))  # 0
        print(int(1 / 3) * 3)  # 0
        print((1 / 3) * 3)  # 1.0
        print((1 / 3) * 3 + 0 / 3)  # 1.0
        print(int((1 / 3) * 3 + 0 / 3))  # 1

    # 测试 or     c == ('+' or '-')   c == '+' or c == '-'
    def testor(self):
        print('+' or '-')  # +
        print('-' or '+')  # -
        c = '+'
        print(c == ('+' or '-'))
        print(c == '+' or c == '-')
        c = '-'
        print(c == ('+' or '-'))
        print(c == '+' or c == '-')

    # 测试 mid的两种不同求法的区别
    def testmid(self):
        low = 0
        n = 10
        for high in range(n):
            # 偶数个数的时候前者往上取整，后者往下取整，奇数个数都是取中间的数
            mid = (high - low + 1) // 2 + low
            mid2 = (high + low) // 2
            print("0 -- ", high, ":", mid, mid2)


t = test()
t.testmid()
# t.testColor()
# t.testor()
# t.numtrans()
