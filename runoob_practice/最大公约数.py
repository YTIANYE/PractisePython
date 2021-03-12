"""

以下代码用于实现最大公约数算法：

"""

num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))

if num1 > num2 :
    num1, num2 = num2, num1

# num1 < num2

# num = 1
# for i in range(1, num1 + 1):
#     if(num1 % i == 0) and (num2 % i == 0):
#         num = i

for i in range(num1 + 1, 1, -1):
    if(num1 % i == 0) and (num2 % i == 0):
        num = i
        break
        pass

print("\n{0}和{1}的最大公约数为：{2}".format(num1, num2, num))
print("\n{0}和{1}的最大公约数为：{2}".format(num1, num2, i))     # 可以调用 i


