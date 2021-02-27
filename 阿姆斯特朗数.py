"""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

以下代码用于检测用户输入的数字是否为阿姆斯特朗数：

"""

while True:

    num = input("请输入要检验的数：")
    weishu = len(str(num))
    temp = weishu
    sum = 0
    while temp > 0:
        n = temp % 10
        sum += n**weishu
        temp //= 10
        pass

    if sum == num:
        print("{}是阿姆斯特朗数".format(num))
    else:
        print("{}不是阿姆斯特朗数".format(num))