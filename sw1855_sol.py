from queue import Queue
from collections import defaultdict
import math

def bfs(tree):
    q = Queue()
    q.put(1)
    ans = []
     
    while q.qsize():
        cur = q.get()
        ans.append(cur)
        if cur in tree:
            for i in tree[cur]:
                q.put(i)
                dp[i][0] = cur
                depth[i] = depth[cur]+1
                 
    return ans
 
     
def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a
 
    for j in range(20, -1, -1):
        if 1<<j <= depth[a] - depth[b]:
            a = dp[a][j]
     
    if a == b: return a
     
    for j in range(19, -1, -1):
        if dp[a][j] != dp[b][j]:
            a = dp[a][j]
            b = dp[b][j]
     
    return dp[a][0]
 
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    parents = list(map(int, input().split()))
    graph = defaultdict(list)
    depth = [0] * (n+1)
    dp = [[0] * 20 for _ in range(n+1)]
     
     
    for i, parent in enumerate(parents):
        graph[parent].append(i+2)
         
    order = bfs(graph)
     
    for i in range(1, 20):
        for x in range(1, n+1):
            dp[x][i] = dp[dp[x][i-1]][i-1]
             
    ans = 0
     
    for i in range(len(order)-1):
        a, b = order[i], order[i+1]
        c = lca(a, b)
        dist = depth[a] + depth[b] - 2 * depth[c]
        ans += dist
        
    print(f'#{test_case} {ans}')