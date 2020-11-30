# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys
from collections import defaultdict

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
sys.stdin = open("sw1849.txt", "r")
'''
class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n
        self.weight = [0] * n
    
    def find(self, index):
        return self.data[index]
    
    def union(self, x, y, weight):
        if y>x:
            x, y = y, x
            weight = -weight

        x_pr, y_pr = self.find(x), self.find(y)

        if x_pr == y_pr :
            return
        for i in range(self.size):
            if self.data[i] == y_pr:
                self.data[i] = x_pr
                self.weight[i] += self.weight[x]+weight

    def find_weight(self, x, y):
        x_pr, y_pr = self.find(x), self.find(y)
        if x_pr == y_pr :
            return str(-self.weight[x]+self.weight[y])
        else:
            return 'UNKNOWN'
'''
def union(a, b, w):
    pa, pb = find(a), find(b)
    
    if pa == pb:
        return
    
    diff = weight[b] - weight[a]

    if rank[pa] > rank[pb]:
        pa, pb = pb, pa
        diff = -diff
        w = -w
    
    weight[pa] = w + diff
    parent[pa] = pb

    if rank[pa] == rank[pb]:
        rank[pb] += 1


def find(a):
    if not parent[a]:
        return a
    else:
        pa = parent[a]
        parent[a] = find(pa)
        weight[a] += weight[pa]
    return parent[a] 
'''
def djset_update(a, b, w):
    a, b, w = int(a), int(b), int(w)
    djset[b] = a
    weight[b] = w
'''    
'''
def find_bfs(start, end):
    start, end = int(start), int(end)
    Q = collections.deque()
    visit = set()
    Q.append(start)
    D={}
    #P = [None]*(N+1)
    #P[start] = start
    D[start] = 0
    while Q:
        start = Q.popleft()
        for i, w in enumerate(adj_mat[start]):
            if w and i not in visit:
                Q.append(i)
                visit.add(i)
                D[i] = D[start] + w
                #P[i] = start
                if i == end:
                    return str(D[i])
    return 'UNKNOWN'
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    N, M = map(int, input().split())
    #adj_mat = [[None]* (N+1) for _ in range(N+1)]
    parent = defaultdict(int)
    weight = defaultdict(int)
    rank = defaultdict(int)
    
    
    #print(command_list[0][0])
    result = []
    for _ in range(M):
        command = input()
        if command[0] == '!':
            a, b, w = map(int, command.split()[1:])
            union(a, b, w)
        elif command[0] == '?':
            a, b = map(int, command.split()[1:])
            if find(a) == find(b):
                result.append(str(weight[a]-weight[b]))
            else:
                result.append('UNKNOWN')
    
    print("#%i %s"%(test_case,' '.join(result)))
    # ///////////////////////////////////////////////////////////////////////////////////
