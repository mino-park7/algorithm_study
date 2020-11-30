

import sys, math

sys.stdin = open("sw10570.txt", "r")
def is_palindrome(N):
    N_str = str(N)
    if N_str == N_str[::-1]:
        return True
    else:
        return False
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    A, B = map(int, input().split())
    if int(math.sqrt(A))**2 - A < 0:
        A_root = int(math.sqrt(A)) + 1
    else:
        A_root = int(math.sqrt(A))
    B_root = int(math.sqrt(B))
    #print(A_root, B_root)
    result = 0

    #print(is_palindrome(1211))
    for N in range(A_root,B_root+1):
        if is_palindrome(N) and is_palindrome(N**2):
            result +=1
    
    print('#%i %i'%(test_case,result))

    # ///////////////////////////////////////////////////////////////////////////////////
