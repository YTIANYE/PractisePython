"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
 

提示：

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
prerequisites[i] 中的所有课程对 互不相同
"""

from collections import defaultdict
from typing import List

# 我实现的官方题解 DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 0未访问，1路径中，2已完成
        flags = [0] * numCourses
        edges = defaultdict(list)   # 
        for a, b in prerequisites:
            edges[b].append(a)
        
        self.has_cycle = False

        def dfs(node):
            if self.has_cycle:
                return
            # 遇到当前路径节点，存在环
            if flags[node] == 1:
                self.has_cycle = True
                return
            # 已遍历完毕，无环
            if flags[node] == 2:
                return
            
            # 进入当前路径，标记为访问中
            flags[node] = 1
            # 遍历所有后继节点
            for neighbor in edges[node]:
                dfs(neighbor)
            # 回溯，当前分支全部遍历完成
            flags[node] = 2
        
        for i in range(numCourses):
            if flags[i] == 0 and not self.has_cycle:    # 加上has_cycle减少不必要遍历
                dfs(i)
        return not self.has_cycle
    

# 我的题解 BFS

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        flags = [0] * numCourses  # 0 未访问 1 访问中 2 访问过
        edges = collections.defaultdict(list)
        for a, b in prerequisites:
            edges[b].append(a)
        # print(edges)

        def level(a):
            if flags[a] == 1:
                return False 
            if flags[a] == 2:
                return True 
            # 未访问时
            flags[a] = 1 
            que = edges[a]
            for b in que:
                if not level(b):
                    return False 
            flags[a] = 2
            return True 

        for i in range(numCourses):
            if not level(i):
                return False 
        return True 
    
# 官方题解 BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses

