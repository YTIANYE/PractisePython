"""
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。

日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。

B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。

C、D、E依次醒来，也按同样的方法拿鱼。

问他们至少捕了多少条鱼?
"""


def fenyu(n):
    for i in range(5):
        if (n - 1) % 5 == 0:
            n = (n - 1) / 5 * 4
        else:
            return 0
    return n


sum = 1

while True:
    if fenyu(sum):
        print("总共有", sum, "条鱼")
        break
    else:
        sum += 1
