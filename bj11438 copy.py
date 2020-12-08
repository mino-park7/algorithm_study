import sys
import time
sys.stdin = open("bj11438.txt", "r")

now = time.time()





N = int(sys.stdin.readline())
# tree[X] 는 X의 조상
tree = [0] * (N+1)

for _ in range(N-1):
    A, B = map(int, sys.stdin.readline().split())
    if tree[B] == 0:
        tree[B] = A
    else:
        tree[A] = B




dp_N = 17

dp = [[0] * (N+1) for _ in range(dp_N)]

dp[0] = tree

#print(dp_N)
for i in range(1, dp_N):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][dp[i-1][j]]
#print(dp)
depth =[0] * (N+1)
for i in range(1, N+1):
    depth_i = 0
    X = i
    for j in range(dp_N-1, -1, -1):
        
        if dp[j][X] != 0 :
            X = dp[j][X]
            depth_i += 2**j
            if X == 1 or X == 0:
                depth[i] = depth_i
#print(depth)
M = int(sys.stdin.readline())
for _ in range(M):
    X, Y = map(int,sys.stdin.readline().split())
    result = 0
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
        result = X
    else:
        for i in range(dp_N-1,-1,-1):
            if dp[i][X] != 0 and dp[i][X] != dp[i][Y]:
                X = dp[i][X]
                Y = dp[i][Y]
            
        result = dp[0][X]
    print(result)

    
print(time.time() - now )
