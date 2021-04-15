"""测试Python"""


class test:

    # Python 三元运算符的替代实现
    def test3operator(self):
        a, b = 5, 2
        maxnum = a if a > b else b
        print(maxnum)


t = test()
t.test3operator()
