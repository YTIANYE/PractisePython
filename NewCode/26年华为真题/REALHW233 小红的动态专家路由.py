"""
描述
有 
N
N 个任务和 
E
E 个专家。每个任务按分数选择前 
K
K 个专家，分数相同优先编号小者。随后按任务编号顺序调度：专家当前负载小于容量 
C
C 时分配生效，否则丢弃。最终输出各专家负载平方和以及负载数组。
输入描述：
第一行输入 
N
,
E
,
K
,
C
N,E,K,C，随后输入 
N
×
E
N×E 的整数评分矩阵。
保证 
N
×
E
≤
5
×
1
0
5
N×E≤5×10 
5
 ，
1
≤
K
≤
E
≤
100
1≤K≤E≤100，
0
≤
C
≤
N
0≤C≤N，评分在 
[
0
,
1
0
4
]
[0,10 
4
 ]。
输出描述：
第一行输出负载平方和，第二行输出各专家最终负载。
示例1
输入：
4 3 2 2
1 5 4
8 1 2
3 6 5
2 7 9
复制
输出：
9
1 2 2
复制
说明：
最终负载为 [1,2,2]。
示例2
输入：
4 4 2 2
5 5 5 1
2 8 8 9
1 2 9 9
7 7 1 1
复制
输出：
13
2 2 1 2
复制
说明：
同分时优先选择编号小的专家。
"""

# 精选题解
import sys

input = sys.stdin.readline

N, E, K, C = map(int, input().split())

# load[i] 表示编号 i+1 的专家当前负载
load = [0] * E

for _ in range(N):
    scores = list(map(int, input().split()))

    # range(E) → [0,1,2,...,E-1] 所有专家下标
    # key=lambda i: (-scores[i], i)
    # 第一关键字：-scores[i] → 分数大的排在前面（降序）
    # 第二关键字：i → 分数相同，专家编号小的排在前面（升序）
    experts = sorted(range(E), key=lambda i: (-scores[i], i))

    # 只取前 K 个专家
    for expert in experts[:K]:
        if load[expert] < C:
            load[expert] += 1

# 计算负载平方和
ans = sum(x * x for x in load)

print(ans)
print(*load)

