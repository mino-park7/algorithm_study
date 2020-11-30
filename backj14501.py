import sys
from collections import deque
sys.stdin = open('backj14501.txt','r')

def dfs(i):
    q = deque()
    result = 0
    #sub_result = 0
    q.append((0,0))

    while q:
        i, sub_result = q.popleft()
        if i == N:
            if result < sub_result:
                result = sub_result
        else:
            for do in range(2):
                if do == 0 :
                    q.append((i+1, sub_result))
                else:    
                    next_i = i+time[i]
                    if next_i > N:
                        next_i = N
                        q.append((next_i,sub_result))
                    else:
                        q.append((next_i, sub_result+pay[i]))
                
    return result



if __name__ == "__main__":
    N = int(input())
    time = []
    pay = []
    for _ in range(N):
        t, p = map(int, input().split())
        time.append(t)
        pay.append(p)

    #print(time)
    #print(pay)

    #result = 0
    #sub_result = 0
    result = dfs(0)
    print(result)