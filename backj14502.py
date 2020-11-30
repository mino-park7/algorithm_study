
import sys
from collections import deque
from itertools import combinations
import copy, time
sys.stdin = open('backj14502.txt','r')

def convection(y,x, virus_map):
    dy, dx = [1,-1,0,0], [0,0,-1,1]
    result = []
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]

        if 0<=ny< N and 0<=nx<M:
            if virus_map[ny][nx] == 0:
                virus_map[ny][nx] = 2
                result.append((ny,nx))
    return result
def equilibrium(virus_map):
    virus_map_temp = copy.deepcopy(virus_map)
    #virus_map_temp = virus_map
    '''
    virus_map_temp_temp = copy.deepcopy(virus_map)
    while True:
        for y in range(N):
            for x in range(M):
                if virus_map_temp[y][x] == 2:
                    convection(y,x,virus_map_temp)
        if virus_map_temp == virus_map_temp_temp:
            break
        else:
            virus_map_temp_temp = copy.deepcopy(virus_map_temp)
    '''
    '''
    for y in range(N):
        for x in range(M):
            if virus_map_temp[y][x] == 2:
                #convection(y,x,virus_map_temp)
                dy, dx = [1,-1,0,0], [0,0,-1,1]

                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]

                    if 0<=ny< N and 0<=nx<M:
                        if virus_map_temp[ny][nx] == 0:
                            virus_map_temp[ny][nx] = 2
    for y in range(N-1,-1,-1):
        for x in range(M-1,-1,-1):
            if virus_map_temp[y][x] == 2:
                #convection(y,x,virus_map_temp)
                dy, dx = [1,-1,0,0], [0,0,-1,1]

                for i in range(4):
                    ny, nx = y+dy[i], x+dx[i]

                    if 0<=ny< N and 0<=nx<M:
                        if virus_map_temp[ny][nx] == 0:
                            virus_map_temp[ny][nx] = 2
    '''
    q = deque()
    q.extend(virus_position)
    while q:
        y, x = q.popleft()
        dy, dx = [1,-1,0,0], [0,0,-1,1]
        #result = []
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]

            if 0<=ny< N and 0<=nx<M:
                if virus_map_temp[ny][nx] == 0:
                    virus_map_temp[ny][nx] = 2
                    q.append((ny,nx))
    
    #return virus_map_temp

    return virus_map_temp

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
    #map_v = {}
    '''
    for y in range(N):
        for x, val in enumerate(list(map(int, input().split()))):
            map_v[(y,x)] = val
    '''
    zero_position = []
    for y in range(N):
        for x in range(M):
            if map_v[y][x] == 0:
                zero_position.append((y,x))
    virus_position = []
    for y in range(N):
        for x in range(M):
            if map_v[y][x] == 2:
                virus_position.append((y,x))
    #print(zero_position)
    combi = combinations(zero_position, 3)
    result = 0
    
    for p1, p2, p3 in combi:
        map_v[p1[0]][p1[1]] = 1
        map_v[p2[0]][p2[1]] = 1
        map_v[p3[0]][p3[1]] = 1
        '''
        map_v[(p1[0],p1[1])] = 1
        map_v[(p2[0],p2[1])] = 1
        map_v[(p3[0],p3[1])] = 1
        virus_map = [[0]*M for _ in range(M)]
        for position, val in map_v.items():
            virus_map[position[0]][position[1]] = val
        '''
        virus_map = equilibrium(map_v)
        sub_result = count_result(virus_map)
        '''
        map_v[(p1[0],p1[1])] = 0
        map_v[(p2[0],p2[1])] = 0
        map_v[(p3[0],p3[1])] = 0
        '''
        map_v[p1[0]][p1[1]] = 0
        map_v[p2[0]][p2[1]] = 0
        map_v[p3[0]][p3[1]] = 0
        if sub_result > result:
            result = sub_result
            #good_shot = shot

    #map_v[1][0] = 1
    #map_v[0][1] = 1
    #map_v[3][5] = 1
    #print(map_v)
    #equilibrium(map_v)
    
    #result = count_result(map_v)        

    #print(map_v)
    print(result)    
    #print(time.time()-now)
