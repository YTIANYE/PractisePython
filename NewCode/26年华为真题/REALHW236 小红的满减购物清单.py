"""
描述
每件商品最多买一件。购物原价每满 200 减 20；若所选商品包含至少 3 个不同类别，则改为每满 200 减 30，两种优惠不叠加。给定预算，求折后价不超过预算时的最大满意度总和。
输入描述：
第一行输入预算，第二行输入商品数 
n
n，随后 
n
n 行输入唯一编号、类别、价格、满意度。
保证预算在 
[
10
,
1000
]
[10,1000]，
1
≤
n
≤
20
1≤n≤20，类别在 
[
1
,
10
]
[1,10]，价格在 
[
1
,
200
]
[1,200]，满意度在 
[
1
,
240
]
[1,240]。
输出描述：
输出最大满意度总和。
示例1
输入：
100
3
10001 1 100 90
10002 2 100 100
10003 3 100 110
复制
输出：
110
复制
说明：
预算只能购买其中一件。
示例2
输入：
200
4
10001 1 200 200
10002 2 10 10
10003 3 10 10
10004 3 10 10
复制
输出：
230
复制
说明：
四件原价 230，三个类别触发减 30，折后正好 200。
"""

# 方法一：二进制枚举法
yusuan = int(input())
n = int(input())
shangpin = []
for i in range(n):
    shangpin.append(list(map(int, input().split())))
# print(shangpin)
# 二进制枚举
res = 0 
for choose in range(1 << n):
    sum_yusuan = 0 
    sum_manyi = 0 
    leibie = set()
    for j in range(n):
        if choose & (1 << j):
            sum_yusuan += shangpin[j][2]
            sum_manyi += shangpin[j][3]
            leibie.add(shangpin[j][1])
    if len(leibie) >= 3:
        discount = (sum_yusuan) // 200 * 30 
    else:
        discount = (sum_yusuan) // 200 * 20
    if sum_yusuan - discount <= yusuan:
        if sum_manyi > res:
            res = sum_manyi
print(res)


# 方法二：DFS
res = 0


def main():

    yusuan = int(input())
    n = int(input())
    shangpin = []
    for i in range(n):
        shangpin.append(list(map(int, input().split())))
    # print(shangpin)
    # 二进制枚举

    def dfs(index, money, manyi, leibie):
        global res
        if n == index:
            if len(leibie) >= 3:
                discount = money // 200 * 30
            else:
                discount = money // 200 * 20
            if money - discount <= yusuan:
                res = max(res, manyi)
            return  # 递归出口
        dfs(index + 1, money, manyi, leibie)
        new_leibie = leibie.copy()  # 注意复制方式
        new_leibie.add(shangpin[index][1])
        dfs(index + 1, money + shangpin[index][2], manyi + shangpin[index][3], new_leibie)


    dfs(0, 0, 0, set())
    print(res)


if __name__ == "__main__":
    main()
