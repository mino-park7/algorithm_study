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
d_p = [(0,1),(0,-1),(-1,0),(1, 0)]
def move(val):
    x, y = val[0] + d_p[val[2]][0], val[1]+d_p[val[2]][1]
    return [x,y,val[2],val[3]]

def dicts(val):
    x, y = val[0], val[1]
    dic[(x,y)].append(val)

sys.stdin = open("sw5648.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    atoms = [list(map(int, input().split())) for _ in range(N)]
    
    energy = 0
    for time in range(2000):
        if len(atoms) < 2:
            break
        dic = defaultdict(list)
        atoms = list(map(move, atoms))
        list(map(dicts, atoms))
        atoms = []
        for i in dic :
            if len(dic[i]) >= 2:
                for item in dic[i]:
                    energy += item[3]
            
            else:
                item = dic[i]
                x = item[0][0]
                y = item[0][1]
                if -1000<=x<=1000 and -1000<=y<=1000:
                    atoms.append(item[0])
    
    print(energy)
            


    
