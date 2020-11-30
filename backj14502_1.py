import sys
from collections import deque
from itertools import combinations
import copy, time
sys.stdin = open('backj14502.txt','r')

def convection(y,x, virus_map):
    dy, dx = [1,-1,0,0], [0,0,-1,1]

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if 0<=ny< N and 0<=nx<M:
            if virus_map[ny][nx] == 0:
                virus_map[ny][nx] = 2

def equilibrium(virus_map):
    temp_virus_map = copy.deepcopy(virus_map)
    while True:
        for y in range(N):
            for x in range(M):
                if virus_map[y][x] == 2:
                    convection(y,x,virus_map)
        if temp_virus_map == virus_map:
            break
        else:
            temp_virus_map = copy.deepcopy(virus_map)
def count_result(virus_map):
    result = 0
    for y in range(N):
        for x in range(M):
            
            if virus_map[y][x] == 0:
                result += 1
    return result
if __name__ == "__main__":
    now = time.time()
    N, M = map(int, input().split())
    map_v = [list(map(int, input().split())) for _ in range(N)]
    
    zero_position = []
    for y in range(N):
        for x in range(M):
            if map_v[y][x] == 0:
                zero_position.append((y,x))
    
    #print(zero_position)
    combi = combinations(zero_position, 3)
    result = 0
    for p1, p2, p3 in combi:
        virus_map = copy.deepcopy(map_v)
        virus_map[p1[0]][p1[1]] = 1
        virus_map[p2[0]][p2[1]] = 1
        virus_map[p3[0]][p3[1]] = 1
        equilibrium(virus_map)
        sub_result = count_result(virus_map)
        if sub_result > result:
            result = sub_result

    #map_v[1][0] = 1
    #map_v[0][1] = 1
    #map_v[3][5] = 1
    #print(map_v)
    #equilibrium(map_v)
    
    #result = count_result(map_v)        

    #print(map_v)
    print(result)    
    print(time.time() - now)