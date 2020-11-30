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
import time
import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open("sw1249.txt", "r")
def move(y,x):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    result = []
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0<=new_x<N and 0<=new_y<N:
            result.append((new_y, new_x))
    return result 

'''
def dfs(y, x):
    global result, sub_result
    visited.append((y,x))
    if sub_result > result:
        return
    
    if y == N-1 and x == N-1:


        if result >= sub_result :
            result = sub_result
            return
        else:
            return

    for new_y, new_x in move(y,x):
        if not (new_y, new_x) in visited:
            sub_result += road[new_y][new_x]
            dfs(new_y, new_x)
            sub_result -= road[new_y][new_x]
'''

def dfs():
    q = deque()
    q.append((0,0))

    while q:
        y, x= q.popleft()
        
        for new_y, new_x in move(y,x):
            w = dp[y][x] + road[new_y][new_x]
            if w < dp[new_y][new_x]:
                dp[new_y][new_x] = w
                q.append((new_y,new_x))
            else:
                continue

                
                    



now = time.time()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    road = [list(map(int,list(input()))) for _ in range(N)]
    dp = [[float('inf')]* N for _ in range(N)]
    dp[0][0] = 0
    dfs()
    #dp1 = [[-1]*N for _ in range(N)]
    '''
    heap = []
    heappush(heap, (0,0,0))

    while heap:
        w, y, x= heappop(heap)
        for new_y, new_x in move(y,x):
            new_w = w+road[new_y][new_x]
            if new_w < dp[new_y][new_x]:
                dp[new_y][new_x] = new_w
                heappush(heap,(new_w,new_y,new_x))
                print(dp)
    '''
    '''
    q = deque()
    q.append((0,0,0))
    while q:
        w, y, x = q.popleft()
        for new_y, new_x in move(y,x):
            new_w = w+road[new_y][new_x]
            if new_w < dp[new_y][new_x]:
                dp[new_y][new_x] = new_w
                q.append((new_w,new_y,new_x))
    '''
    print(dp[-1][-1])

print(time.time() - now)