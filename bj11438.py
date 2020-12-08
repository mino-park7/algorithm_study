import sys
from collections import deque
sys.stdin = open("bj11438.txt", "r")
import time
now = time.time()

def bfs(start, edges, tree, depth):
    visited = [False] * (len(tree))
    q = deque()

    q.append(1)
    visited[1] = True
    while q:
        node = q.pop()
        for node2 in edges[node]:
            
                if not visited[node2]: 
                    tree[node2] = node
                    q.append(node2)
                    visited[node2] = True
                    depth[node2] = depth[node] +1




def LCA(X, Y, dp, depth, dp_N):

    dep_X = depth[X]
    dep_Y = depth[Y]

    if dep_X < dep_Y:
        X ,Y = Y, X
        dep_X, dep_Y = dep_Y, dep_X

    
    dist = dep_X - dep_Y

    while dist != 0:
        i = len(bin(dist)) - 3
        
        X = dp[i][X]
        dep_X = depth[X]
        dist = dep_X - dep_Y

    if X == Y:
        return X
    else:
        for i in range(dp_N-1,-1,-1):
            if dp[i][X] != 0 and dp[i][X] != dp[i][Y]:
                X = dp[i][X]
                Y = dp[i][Y]
            
        return dp[0][X]

    

        






N = int(sys.stdin.readline())
# tree[X] 는 X의 조상
tree = [0] * (N+1)
edges = {}
for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    try:
        edges[A].append(B)
    except :
        edges[A] = []
        edges[A].append(B)
    try:
        edges[B].append(A)
    except:
        edges[B] = []
        edges[B].append(A)
depth = [0] * (N+1) 
bfs(1, edges, tree, depth)



dp_N = 17

dp = [[0] * (N+1) for _ in range(dp_N)]

dp[0] = tree

#print(dp_N)
for i in range(1, dp_N):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][dp[i-1][j]]
#print(dp)
#depth = [find_depth(i, dp, dp_N) for i in range(N+1)]
#print(depth)
M = int(sys.stdin.readline())
for _ in range(M):
    X, Y = map(int,sys.stdin.readline().split())
    print(LCA(X,Y, dp, depth,dp_N))

    
print(time.time() - now)
