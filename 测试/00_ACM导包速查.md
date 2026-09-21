# ACM 导包速查（从 LeetCode 搬到 ACM 要补什么）

> 牛客 / Codeforces 等 OJ 不会像 LeetCode 那样隐式提供数据结构与类型，
> 下面按「需要 import 的内容 + 用法」整理，刷题时按需取用。

## 0. 先记住三条

1. **LeetCode 隐式提供的，ACM 都要自己写**：`ListNode`、`TreeNode`、`List`/`Optional` 类型标注、`Solution` 类外壳。
2. **类型标注 `List` / `Optional` 在 ACM 可以整个删掉**，不必导入；真要留就 `from typing import List, Optional`。
3. **第三方库多数 OJ 没有**：`numpy`、`torch`、`sortedcontainers` 别依赖（见第 3 节）。

---

## 1. 标准库模块 → 用法

### sys（输入输出的基础，必会）
```python
import sys
input = sys.stdin.readline          # 替换内置 input，大输入更快（字符串记得 .strip()）
data = sys.stdin.read().split()     # 一次性读全部，配指针解析
sys.stdout.write("\n".join(out))    # 大量输出攒批，比反复 print 快
sys.setrecursionlimit(10**6)        # 树/图 DFS 深递归必加，否则 RecursionError
```

### math（数学常用）
```python
import math
math.sqrt(x)            # 开方
math.gcd(a, b)          # 最大公约数
math.lcm(a, b)          # 最小公倍数（Python 3.9+）
math.comb(n, k)         # 组合数 C(n,k)（3.8+，枚举组合超方便）
math.factorial(n)       # 阶乘
math.pi / math.e
math.ceil(x) / math.floor(x)
math.log(x) / math.log2(x)
```

### collections（容器三件套）
```python
from collections import defaultdict, deque, Counter
d = defaultdict(int)            # 默认 0；也可 defaultdict(list)
q = deque([...])                # BFS 队列，popleft()/append()，O(1)
c = Counter(arr)                # 计数；c.most_common(k) 取前 k 频繁
```

### heapq（堆 / 优先队列）
```python
import heapq
heapq.heappush(h, x)            # 入堆（默认小根堆）
heapq.heappop(h)                # 弹出最小值
heapq.heapify(arr)              # 原地建堆
heapq.nlargest(k, arr) / nsmallest(k, arr)
# 大根堆技巧：存 -x
```

### itertools（排列组合枚举）
```python
from itertools import permutations, combinations, product, accumulate
list(permutations(arr, k))      # 全排列
list(combinations(arr, k))      # 组合
product(arr, repeat=k)          # 笛卡尔积（枚举所有选择）
list(accumulate(arr))           # 前缀和
```

### bisect（二分查找 / 维护有序序列）
```python
import bisect
bisect.bisect_left(a, x)        # 第一个 >= x 的位置
bisect.bisect_right(a, x)       # 第一个 > x 的位置
bisect.insort(a, x)             # 插入并保持有序
```

### functools（记忆化）
```python
from functools import lru_cache, reduce
@lru_cache(None)                # 记忆化递归，爆搜/DP 提速
def f(...): ...
reduce(lambda a, b: a*b, arr)  # 累积
```

### re（字符串正则）
```python
import re
re.findall(r'\d+', s)           # 提取数字
re.split(r'\s+', s)
```

### string / random（按需）
```python
import string
string.ascii_lowercase          # 'abcdef...'
string.digits                   # '0123456789'

import random                   # 随机化算法/交互题偶尔用
random.randint(a, b); random.shuffle(arr)
```

### typing（仅类型标注，可删）
```python
from typing import List, Optional   # 若保留标注就导入，否则整行删掉
```

---

## 2. LeetCode 隐式提供 → ACM 需自备的定义

直接粘到代码顶部即可。

```python
# 单链表结点（LeetCode 标准定义）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 二叉树结点（LeetCode 标准定义）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

> 注意：你的 `剑指 Offer_practice/tree.py` 里 `TreeNode(val=-1)` 默认值不同，
> 但 ACM 用上面标准版即可；刷题时按题目给的定义为准。

可选辅助（本地调试建树/建链表）：
```python
# 数组 -> 链表
def arr_to_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0]); cur = head
    for v in arr[1:]:
        cur.next = ListNode(v); cur = cur.next
    return head

# 层序数组 -> 二叉树（按 LeetCode 的 [1,2,null,3] 形式）
import sys
def arr_to_tree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0]); q = [root]; i = 1
    while q and i < len(arr):
        node = q.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i]); q.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i]); q.append(node.right)
        i += 1
    return root
```

---

## 3. 不可用 / 慎用（OJ 一般没有）

| 模块 | 说明 | ACM 替代 |
|------|------|----------|
| `sortedcontainers.SortedList` | 你的 295/456 题用过，多数 OJ 装不了 | `bisect` + 列表，或手写堆/平衡树 |
| `numpy` | 矩阵题别依赖 | 用嵌套 `list` |
| `torch` | 深度学习库，OJ 没有 | — |

> 写 ACM 代码时默认只用**标准库**；遇到上述第三方库，先想标准库怎么替。
