"""
描述
一条左右两端开口的直线水槽中，从左到右有 
n
n 块高度为 
h
i
h 
i
​
  的竖直挡板。相邻挡板间形成单位底面积槽位，雨水充足并达到稳定。求所有 
n
−
1
n−1 个槽位中的水量之和。
输入描述：
第一行输入 
n
n，第二行输入 
n
n 个挡板高度。保证 
1
≤
n
≤
30000
1≤n≤30000，
1
≤
h
i
≤
30000
1≤h 
i
​
 ≤30000。
输出描述：
输出稳定后的总存水量。
示例1
输入：
5
1 2 3 4 5
复制
输出：
10
复制
说明：
四个槽位水面高度依次为 1、2、3、4。
示例2
输入：
6
3 1 2 5 4 5
复制
输出：
19
复制
说明：
五个槽位水面高度依次为 3、3、3、5、5。
"""

def solve(n, h):
    maxleft = [0] * n
    maxright = [0] * n
    res = 0
    for i in range(n):
        j = n - 1 - i
        if i == 0:
            maxleft[i] = h[i]
            maxright[j] = h[j]
        else:
            maxleft[i] = max(maxleft[i - 1], h[i])
            maxright[j] = max(maxright[j + 1], h[j])
    # 注意计算方式
    for i in range(n-1):
        res += min(maxleft[i], maxright[i+1])
    return res


if __name__ == "__main__":
    n = list(map(int, input().split()))[0]
    h = list(map(int, input().split()))
    res = solve(n, h)
    print(res)
