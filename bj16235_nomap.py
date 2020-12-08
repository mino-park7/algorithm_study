import sys
#from collections import deque
#input = sys.stdin.readline
import time
now = time.time()
sys.stdin = open("bj16235.txt", "r")
N, M , K = map(int, input().split())
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,0,1,-1]

def tree_plant(x,y,z, tree):
    tree[x][y].append(z)
    '''
    try:
        tree[(x,y)].append(z)
    except:
        tree[(x,y)] = []
        tree[(x,y)].append(z)
    #tree[(x,y)].sort()
    '''

def spring(soil, tree:dict, dead_tree:dict):
    del_list=[]
    result = []
    for x in range(N):
        for y in range(N):

            
            key = (x,y)
            len_val = len(tree[x][y])
            for i, age in enumerate(tree[x][y][::-1]):
                if age <= soil[key[0]][key[1]]:
                    soil[key[0]][key[1]] -= age
                    tree[x][y][len_val-i-1] += 1
                    if tree[x][y][len_val-i-1] % 5 == 0:
                        result.append(key)
                else:
                    '''
                    for dead in val[:len_val-i]:
                        tree_plant(key[0], key[1], dead, dead_tree)
                    '''
                    dead_tree[key] = tree[x][y][:len_val-i]
                    if i > 0:
                        tree[x][y] = tree[x][y][len_val-i:]
                    else:
                        tree[x][y] = []
                    break
    
    
    return result
def summer(soil, dead_tree):
    for key, val in dead_tree.items():
        for age in val:
            soil[key[0]][key[1]] += age//2
    
    
def fall(soil, tree, growth_list):
    #growth_list=[]
    def _growth(x, y, tree):
        #dx, dy = [-1,0,1],[-1,0,1]
        for i in range(8):
            ddx = dx[i]
            ddy = dy[i]
        
            if 0<=x+ddx<N and 0<=y+ddy<N:
                tree_plant(x+ddx, y+ddy, 1, tree)
    '''
    for key, val in tree.items():
        for age in val:
            if age % 5 == 0:
                growth_list.append(key)
    '''
    for key in growth_list:
        _growth(key[0], key[1], tree)

def winter(soil, tree:dict, A):
    for i in range(N):
        for j in range(N):
            soil[i][j] += A[i][j]
    



soil = [[5]*N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)] 
dead_tree = {}
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_plant(x-1,y-1, z, tree)

for _ in range(K):
    growth_list = spring(soil, tree, dead_tree)
    summer(soil, dead_tree)
    dead_tree = {}
    fall(soil, tree, growth_list)
    winter(soil, tree, A)

'''
for _ in range(K):
    # spring
    #del_list=[]
    growth_list = []
    for x in range(N):
        for y in range(N):

            
            key = (x,y)
            len_val = len(tree[x][y])
            for i, age in enumerate(tree[x][y][::-1]):
                if age <= soil[key[0]][key[1]]:
                    soil[key[0]][key[1]] -= age
                    tree[x][y][len_val-i-1] += 1
                    if tree[x][y][len_val-i-1] % 5 == 0:
                        growth_list.append(key)
                else:
                    
                    dead_tree[key] = tree[x][y][:len_val-i]
                    if i > 0:
                        tree[x][y] = tree[x][y][len_val-i:]
                    else:
                        tree[x][y] = []
                    break
    # summer
    for key, val in dead_tree.items():
        for age in val:
            soil[key[0]][key[1]] += age//2
    dead_tree = {}
    # fall

    for key in growth_list:
        x, y = key[0], key[1]
        
        for i in range(8):
            ddx = dx[i]
            ddy = dy[i]
            if ddx==0 and ddy==0:
                pass
            else:
                if 0<=x+ddx<N and 0<=y+ddy<N:
                    tree_plant(x+ddx, y+ddy, 1, tree)
    
    #winter
    for i in range(N):
        for j in range(N):
            soil[i][j] += A[i][j]
'''


result = 0
for x in range(N):
    for y in range(N):
        
        result += len(tree[x][y])

print(result)
print(time.time() - now )