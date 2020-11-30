

import sys
from collections import defaultdict, deque
sys.stdin = open("sw1248.txt", "r")

def bfs(start):
    q = deque()
    #visited = []
    q.append(start)
    count = 0
    while q :
        s = q.popleft()
        count += 1
        #visited.append(s)
        if graph[s]:
            for j in graph[s]:
                q.append(j)
                depth[j] = depth[s] + 1
                dp[0][j] = s
    return count
def lca(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    for j in range(20,-1,-1):
        if 1<<j <= depth[a]-depth[b]:
            a = dp[j][a]
    
    if a == b:
        return a
    
    for j in range(19,-1,-1):
        if dp[j][a] != dp[j][b]:
            a = dp[j][a]
            b = dp[j][b]
        
    return dp[0][a]


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.
    '''
    V, E, a, b = map(int, input().split())
    E_list = list(map(int, input().split()))

    graph = defaultdict(list)
    depth = [0]*(V+1)
    for i in range(E):
        graph[E_list[2*i]].append(E_list[2*i+1])
    dp = [[0]*(V+1) for _ in range(20)]
    #print(graph)
    _ = bfs(1)
    
    for k in range(1,20):
        for i in range(E+2):
            dp[k][i] = dp[k-1][dp[k-1][i]]
    #print(dp)
    print('#%i %i %i'%(test_case, lca(a,b), bfs(lca(a,b))))
    # ///////////////////////////////////////////////////////////////////////////////////
