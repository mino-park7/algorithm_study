import sys
from math import log2
from collections import deque
import time
now = time.time()
sys.stdin = open("bj11438.txt", "r")
N=int(sys.stdin.readline())
logN=int(log2(N)+1)
tree=[[] for _ in range(N+1)]#각 노드의 부모노드 저장
for _ in range(N-1):
    p,c=map(int,sys.stdin.readline().split())
    tree[c].append(p)
    tree[p].append(c)
 
p_list=[0 for _ in range(N+1)]#부모노드 저장
depth=[0 for _ in range(N+1)]#부모노드 개수
 
p_check=[True for _ in range(N+1)]#DFS를 위해 사용
#dfs로 모든 노드의 부모노드 찾기
q=deque()
q.append(1)
while q:
    p=q.popleft()
    p_check[p]=False
    for i in tree[p]:
        if p_check[i]:
            q.append(i)
            p_list[i]=p
            depth[i]=depth[p]+1#깊이도 같이 저장해준다.

 
#2^k번째 부모노드 저장
#log2 1000000=16.6096...
DP=[[0 for _ in range(logN)] for i in range(N+1)]
#초기화
for i in range(N+1):
    DP[i][0]=p_list[i]
 
for j in range(1,logN):
    for i in range(1,N+1):
        # if DP[DP[i][j-1]][j-1]!=0:
            DP[i][j]=DP[DP[i][j-1]][j-1]
  
 
M=int(sys.stdin.readline())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if depth[a]>depth[b]:
        a,b=b,a
    #둘의 차이를 구하여 레벨 맞춰주기
    dif=depth[b]-depth[a]
    #b의 dif조상 찾기
    for i in range(logN):
        if dif & 1<<i: #ex dif의 11번째 부모노드를 구할 경우 경우 dif = 1011(2) b=DP[DP[DP[b][0]][1]][3]
            b=DP[b][i]
 
    if a==b:
        print(a)
        continue
 
 
    for i in range(logN-1,-1,-1):
        if DP[a][i]!=DP[b][i]:#처음으로 같지않은 부분으로가 가서 다시 검색
            a=DP[a][i]
            b=DP[b][i]
 
    print(DP[b][0])
 
print(time.time() - now)