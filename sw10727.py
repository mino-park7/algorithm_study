

import sys


sys.stdin = open("sw10727.txt", "r")

def is_biggest():
    rlt = 0
    #zero_list = []
    for r in range(N):
        for c in range(M):
            if map_rad[r][c] == col_max[c] and map_rad[r][c] == row_max[r]:
                
                #zero_list.append((r,c))
                rlt += 1
    
   

    return rlt


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, P = map(int, input().split())
    map_rad = [list(map(int, input().split())) for _ in range(N)]
    col_max = [0] * M
    row_max = [max(row) for row in map_rad ]
    for row in map_rad:
        for i, val in enumerate(row):
            if val > col_max[i]:
                col_max[i] = val
    '''
    map_rad_inv = [[0] * N for _ in range(M)]
    for r in range(N):
        for c in range(M):
            map_rad_inv[c][r] = map_rad[r][c]
    col_max = [max(col) for col in map_rad_inv]
    '''
    result = 0
    
    

    for _ in range(P):
        r, c, x = map(int, input().split())
        r -= 1
        c -= 1

        map_rad[r][c] = x
        #map_rad_inv[c][r] = x
        if col_max[c] < x:
            col_max[c] = x
        if row_max[r] < x:
            row_max[r] = x

        result += is_biggest()

    print("#%i %i"%(test_case, result))
        
