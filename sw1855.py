

import sys
from collections import deque, defaultdict
#import math
'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("sw1855.txt", "r")

def bfs():
    visited = []
    q = deque()
    #dis = 0
    #t = []
    q.append(1)
    while q:
        s = q.popleft()
        #if len(visited) != 0:
            #dis += dist(s,visited[-1])
        visited.append(s)
        #t.append(s)
        if s in graph:
            for i in graph[s]:
                q.append(i)
                depth_list[i] = depth_list[s] +1
    
    return visited
'''
def dist(a, b):
    def _find_anc(x):
        anc = [x]
        
        while not x == tree[x]:
            x = tree[x]
            anc.append(x)
        return anc
    
    anc_a = _find_anc(a)
    anc_b = _find_anc(b)

    com = list(set(anc_a) & set(anc_b))[-1]
    #print(com)
    result = anc_a.index(com) + anc_b.index(com)
    return result
'''

def lca(a, b):
    if depth_list[a] < depth_list[b]:
        a, b = b, a
    #diff = depth_list[a]-depth_list[b]
    
    for j in range(max_log_depth,-1,-1):
        if 1<<j <= depth_list[a]-depth_list[b]:
            a = dp[j][a]
    if a == b :
        return a
    
    for j in range(max_log_depth-1,-1,-1):
        if dp[j][a] != dp[j][b]:
            a = dp[j][a]
            b = dp[j][b]
    return dp[0][a]
    
def dist(a,b):
    com_anc = lca(a,b)
    result = -2*depth_list[com_anc] + depth_list[a] + depth_list[b]
    return result


'''
def find_depth(x):
    depth = 0
    while not tree[x] == 0:
        x = tree[x]
        depth +=1
    return depth
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N = int(input())
    tree = [0, 0] + list(map(int, input().split()))
    graph = defaultdict(list)
    for i, parent in enumerate(tree):
        graph[parent].append(i)
    depth_list = [0] * (N+1)
    #for node in range(2,N+1):
    #    depth_list.append(find_depth(node))
    #print(tree)
    #
    #print(visited)
    #print(dist(3,4))
    #dis = 0
    #for i in range(len(visited)-1):
    #    dis += dist(visited[i],visited[i+1])
    #print(depth_list)
    dp = [[0]* (N+1) for _ in range(20)]
    #print(int(math.log2(max(depth_list[2:]))))
    max_log_depth = 20
    '''
    for k in range(max_log_depth):
    
        k_tree = []

        for i in range(N+1):
            k_tree.append(dp[-1][dp[-1][i]])
        dp.append(k_tree)
        #print(k_tree)
    '''
    for k in range(max_log_depth):
        for i in range(N+1):
            if k == 0:
                dp[k][i] = tree[i]
            else:
                dp[k][i] = dp[k-1][dp[k-1][i]]
        #print(dp)
    #print(dp)
#    if test_case==3:
#        print(lca(10,4))

    visited = bfs()
    dis = 0
    for i in range(len(visited)-1):
        dis += dist(visited[i],visited[i+1])
    print('#%i %i'%(test_case,dis))
    # ///////////////////////////////////////////////////////////////////////////////////
