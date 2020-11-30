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
sys.stdin = open("sw1252.txt", "r")
def conv_2d(filter_size, S):
    #global fix_position
    
    if filter_size == 1:
        min_count = 1
    elif filter_size == 2:
        min_count = 2
    elif filter_size == 3:
        min_count = 5
    else:
        min_count = 0
    '''
    if filter_size == 1:
        count = 1
    elif filter_size == 2:
        count = 3
    elif filter_size == 3:
        count = 6
    else:
        count = 0
    '''
    max_count = filter_size*filter_size
    result = defaultdict(bool)
    for count in range(max_count,min_count-1,-1):
        for row in range(1, S+1-filter_size+1):
            for col in range(1, S+1-filter_size+1):
                '''
                if filter_size == 3 and count ==7:
                    filter_position = 2
                    if (fix_position[(row,col)] or fix_position[(row+1,col)] or fix_position[(row+2,col)]) and (fix_position[(row,col)] or fix_position[(row,col+1)] or fix_position[(row,col+2)]) and ((fix_position[(row,col)] or fix_position[(row+1,col)] or fix_position[(row,col+1)]) and (fix_position[(row+filter_position,col)]or fix_position[(row+filter_position -1 ,col)] or fix_position[(row+filter_position,col+1)]) and (fix_position[(row+filter_position,col+filter_position)] or fix_position[(row+filter_position-1,col+filter_position)] or fix_position[(row+filter_position,col+filter_position-1)]) and (fix_position[(row,col+filter_position)] or fix_position[(row+1,col+filter_position)] or fix_position[(row,col+filter_position-1)]))== True:
                        result[(row,col)] = True
                        erase(row,col,filter_size)
                        continue
                '''    
                filter_count = 0
                for i in range(filter_size):
                    for j in range(filter_size):
                        if fix_position[(row+i,col+j)]:
                            filter_count +=1
                if filter_count >= count:
                    result[(row,col)] = True
                    erase(row,col,filter_size)
    
        '''
        new_fix_position = defaultdict(bool)
        for key, value in fix_position.items():
            
            if value:
                new_fix_position[key] = value
        fix_position = new_fix_position
        '''     
    return result      

'''
def del_overlap(filter3,filter2,filter1):
    for i,j in filter3:
'''
def erase(row, col, filter_size):
    for i in range(filter_size):
        for j in range(filter_size):
            if fix_position[(row+i, col+j)]:
                del fix_position[(row+i, col+j)]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    S = int(input())
    N = int(input())
    fix_position = defaultdict(bool)
    fix_list = list(map(int, input().split()))

    for i in range(N):
        fix_position[(fix_list[2*i], fix_list[2*i+1])] = True

   
    result_3d = conv_2d(3,S)    
    result_2d = conv_2d(2,S)
    result_1d = conv_2d(1,S)
    print(test_case, len(result_3d)*7+len(result_2d)*4+len(result_1d)*2)
    #print(test_case, result_2d)
    #print(test_case, result_1d)
    '''
    result = []
    for i,j in result_3d:
        result.append(str(i))
        result.append(str(j))
        result.append('3') 
    for i,j in result_2d:
        result.append(str(i))
        result.append(str(j))
        result.append('2') 
    for i,j in result_1d:
        result.append(str(i))
        result.append(str(j))
        result.append('1')
    print("#%i %i %s"%(test_case,len(result_3d)+len(result_2d)+len(result_1d), " ".join(result))) 
    # ///////////////////////////////////////////////////////////////////////////////////
    '''