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
        print(1 / 3)                        # 0.3333333333333333
        print(int(1 / 3))                   # 0
        print(int(1 / 3) * 3)               # 0
        print((1 / 3) * 3)                  # 1.0
        print((1 / 3) * 3 + 0 / 3)          # 1.0
        print(int((1 / 3) * 3 + 0 / 3))     # 1

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



t = test()
# t.testColor()
t.testor()
# t.numtrans()
