import sys
#from collections import deque
#input = sys.stdin.readline
import time
now = time.time()
sys.stdin = open("bj16235.txt", "r")
N, M , K = map(int, input().split())
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,0,1,-1]

def tree_plant(x,y,z, tree, count):
    try:
        tree[x][y][z] += count
    except:
        tree[x][y][z] = count 
    '''
    try:
        tree[(x,y)].append(z)
    except:
        tree[(x,y)] = []
        tree[(x,y)].append(z)
    #tree[(x,y)].sort()
    '''

def spring(soil, tree, dead_tree:dict):
    #del_list=[]
    age_list = []
    for x in range(N):
        for y in range(N):

            
            
            for age in sorted(tree[x][y].keys()):
                if age <= soil[x][y]:
                    if age * tree[x][y][age] <= soil[x][y]:
                        soil[x][y] -= age * tree[x][y][age]
                        #tree[x][y][age + 1] = tree[x][y][age]
                        age_list.append((x,y,age+1,tree[x][y][age]))
                        #tree_plant(x,y,age+1, tree, tree[x][y][age])
                        del tree[x][y][age]
                    else:
                        share = soil[x][y] // age
                        soil[x][y] -= age * share
                        #tree[x][y][age + 1] = share
                        #tree_plant(x,y, age+1, tree, share)
                        age_list.append((x,y,age+1,share))
                        tree[x][y][age] -= share
                        
                        dead_tree[(x,y,age)] = tree[x][y][age]
                        
                        del tree[x][y][age]
                else:
                    '''
                    for dead in val[:len_val-i]:
                        tree_plant(key[0], key[1], dead, dead_tree)
                    '''
                    
                    dead_tree[(x,y,age)] = tree[x][y][age]
                    
                    del tree[x][y][age]
    for x,y,age,count in age_list:
        tree_plant(x,y,age,tree,count)
    
def summer(soil, dead_tree):
    for key, val in dead_tree.items():
            soil[key[0]][key[1]] += (key[2]//2) * val
    
    
def fall(soil, tree):
    #growth_list=[]
    def _growth(x, y, tree, count):
        #dx, dy = [-1,0,1],[-1,0,1]
        for i in range(8):
            ddx = dx[i]
            ddy = dy[i]
        
            if 0<=x+ddx<N and 0<=y+ddy<N:
                tree_plant(x+ddx, y+ddy, 1, tree, count)
    '''
    for key, val in tree.items():
        for age in val:
            if age % 5 == 0:
                growth_list.append(key)
    '''
    for x in range(N):
        for y in range(N):
            for age, val in tree[x][y].items():
                if age % 5 == 0:
                    _growth(x, y, tree, val)

def winter(soil, tree:dict, A):
    for i in range(N):
        for j in range(N):
            soil[i][j] += A[i][j]
    



soil = [[5]*N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[{} for _ in range(N)] for _ in range(N)] 
dead_tree = {}
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_plant(x-1,y-1, z, tree, 1)

for _ in range(K):
    spring(soil, tree, dead_tree)
    summer(soil, dead_tree)
    dead_tree = {}
    fall(soil, tree)
    winter(soil, tree, A)



result = 0
for x in range(N):
    for y in range(N):
        for count in tree[x][y].values():
            result += count

print(result)
print(time.time() - now )