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
        color = '#' + str("%03d" % random.randint(0, 255))[2:] + str("%03d" % random.randint(0, 255))[2:] + str("%03d" % random.randint(0, 255))[2:]
        print(color)

        c = "137"
        c2 = c[2:]
        print(c2)




t = test()
t.testColor()
