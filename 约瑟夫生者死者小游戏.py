"""
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
"""

li = [0]
num = 30
shu = 9

for i in range(num):
    li.append(i+1)

print(li)

i = 1
while num > 15:
    i += 8
    if i > num:
        i %= num

    print(li[i], "号下船了")
    li.remove(li[i]) # remove()  中填的是元素值，不是元素索引
    # print(li)
    num -= 1

print(li)
