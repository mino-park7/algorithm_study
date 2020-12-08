import sys

sys.stdin = open("bj3584.txt", "r")

T = int(input())

def find_depth(X, tree):
    depth = 0
    while tree[X] != 0:
        X = tree[X]
        depth += 1
    
    return depth

def LCA(X, Y, dp, depth):

    dep_X = depth[X]
    dep_Y = depth[Y]

    if dep_X < dep_Y:
        X ,Y = Y, X
        dep_X, dep_Y = dep_Y, dep_X

    
    dist = dep_X - dep_Y

    while dist != 0:
        i = 0
        while dist != 1:
            dist = dist >> 1
            i += 1
        
        X = dp[i][X]
        dep_X = depth[X]
        dist = dep_X - dep_Y

    if X == Y:
        return X
    else:
        for i in range(19,-1,-1):
            if dp[i][X] != 0 and dp[i][X] != dp[i][Y]:
                X = dp[i][X]
                Y = dp[i][Y]
            
        return dp[0][X]

    

        





for test_case in range(1,T+1):
    N = int(input())
    # tree[X] 는 X의 조상
    tree = [0] * (N+1)
    
    for _ in range(N-1):
        A, B = map(int, input().split())

        tree[B] = A

    X, Y = map(int,input().split())


    dp = [[0] * (N+1) for _ in range(20)]

    dp[0] = tree
    depth = [find_depth(i, tree) for i in range(N+1)]
    #print(dp)

    for i in range(1, 20):
        for j in range(1, N+1):
            dp[i][j] = dp[i-1][dp[i-1][j]]
    

    print(LCA(X,Y, dp, depth))
    
        



