"""测试Python"""
import random


class test:
    """Python 三元运算符的替代实现"""

    def test3operator(self):
        a, b = 5, 2
        maxnum = a if a > b else b
        print(maxnum)

    """测试随机合成color [2: ] 三位中截取最后一个数字"""

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

    """测试 or     c == ('+' or '-')   c == '+' or c == '-'"""

    def testor(self):
        print('+' or '-')  # +
        print('-' or '+')  # -
        c = '+'
        print(c == ('+' or '-'))
        print(c == '+' or c == '-')
        c = '-'
        print(c == ('+' or '-'))
        print(c == '+' or c == '-')

    """测试 mid的两种不同求法的区别"""

    def testmid(self):
        low = 0
        n = 10
        for high in range(n):
            # 偶数个数的时候前者往上取整，后者往下取整，奇数个数都是取中间的数
            mid = (high - low + 1) // 2 + low
            mid1 = (high - low) // 2 + low
            mid2 = (high + low) // 2
            print("0 -- ", high, ":", mid, mid1, mid2)  # mid1和mid2等同

    """测试 不定长参数"""

    def test_Indefinite_length_parameter(self):
        """含有不定长参数的函数"""

        # 方式一： 元组
        def test_parameter(*para):
            p = para[0] if para else None
            if p:  # 是None的时候不会打印
                print(p)
            # for p in para:
            #     print(p)

        test_parameter()  # 不传入也没有关系，即空元组也没有关系
        test_parameter(1)

        # para = (0,)
        # test_parameter(para)
        # para2 = (1, 0)
        # test_parameter(para2)

        # 方式二：字典
        def test_parameter2(**para):
            print(para)
        # test_parameter2(a=2)

    """测试移位运算 """

    def test_displacement(self):
        for i in range(10):
            print(1 << i)   # 1 2 4 8 ...


if __name__ == "__main__":
    """初始化对象"""
    t = test()

    """测试"""
    # 测试移位运算
    t.test_displacement()


    # 测试不定长参数
    # t.test_Indefinite_length_parameter()

    # 测试 mid的两种不同求法的区别
    # t.testmid()
    # t.testColor()
    # t.testor()
    # t.numtrans()
