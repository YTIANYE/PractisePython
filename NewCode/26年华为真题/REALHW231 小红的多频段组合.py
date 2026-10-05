"""
描述
小红从 
N
N 个候选载波中选择至多 
K
K 个。每个载波有带宽和频段；同一频段最多选一个，给定的冲突频段也不能同时出现。最大化总带宽。若最优方案不唯一，输出升序编号序列中字典序最小的一组。频段名不区分大小写。
输入描述：
第一行输入 
N
,
K
N,K；第二行输入带宽；第三行输入频段名；第四行输入冲突对数 
C
C，随后 
C
C 行输入冲突频段对。
保证 
1
≤
N
≤
25
1≤N≤25，
1
≤
K
≤
min
⁡
(
8
,
N
)
1≤K≤min(8,N)，带宽在 
[
1
,
1000
]
[1,1000]，
0
≤
C
≤
25
0≤C≤25，频段名长度不超过 10。
输出描述：
第一行输出最大总带宽，第二行输出所选载波编号（从 0 开始，升序）。
示例1
输入：
6 2
100 200 150 300 250 180
n78 n41 n78 n28 n41 n28
1
n28 n41
复制
输出：
450
2 3
复制
说明：
编号 2 与 3 分属不冲突频段，总带宽 450。
示例2
输入：
3 2
10 10 10
n1 n2 n3
0
复制
输出：
20
0 1
复制
说明：
等带宽方案中字典序最小的是 [0,1]。
"""

def main():
    import sys
    input = sys.stdin.read().splitlines()
    ptr = 0
    N, K = map(int, input[ptr].split())
    ptr += 1
    bw = list(map(int, input[ptr].split()))
    ptr += 1
    band = input[ptr].split()
    ptr += 1
    # 频段全部转小写，不区分大小写
    band = [s.lower() for s in band]
    C = int(input[ptr])
    ptr += 1
    conflict = dict()
    for _ in range(C):
        a,b = input[ptr].split()
        ptr +=1
        a = a.lower()
        b = b.lower()
        if a not in conflict:
            conflict[a] = set()
        conflict[a].add(b)
        if b not in conflict:
            conflict[b] = set()
        conflict[b].add(a)
    
    max_total = -1
    best_sel = []

    # DFS: idx 当前载波，selected已选下标列表，used_bands 已选用频段集合，sum_bw总带宽
    def dfs(idx, selected, used_bands, sum_bw):
        nonlocal max_total, best_sel
        # 更新答案：至多K个，只要当前组合更好就更新；总和相等取字典序更小（先搜到的，因为从小到大遍历）
        if sum_bw > max_total:
            max_total = sum_bw
            best_sel = selected.copy()
        # 剪枝
        if idx >= N:
            return
        if len(selected) >= K:
            return
        
        # 尝试选当前载波 idx
        bname = band[idx]
        ok = True
        # 规则1：同一频段最多选一个
        if bname in used_bands:
            ok = False
        # 规则2：不能和已选的频段冲突
        if ok and bname in conflict:
            for ub in used_bands:
                if ub in conflict[bname]:
                    ok = False
                    break
        if ok:
            selected.append(idx)
            used_bands.add(bname)
            dfs(idx+1, selected, used_bands, sum_bw + bw[idx])
            used_bands.remove(bname)
            selected.pop()
        # 不选当前载波
        dfs(idx+1, selected, used_bands, sum_bw)

    dfs(0, [], set(), 0)
    print(max_total)
    print(' '.join(map(str, best_sel)))

if __name__ == "__main__":
    main()
