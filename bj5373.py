import sys
sys.stdin = open("bj5373.txt", "r")
T = int(input())




def process_command(command_list, U, D, F, B, L, R):
    for command in command_list:
        roll(command[0], command[1], U, D, F, B, L, R)
        '''
        if command[0] == "U":
            roll(U, command[1])
        if command[0] == "D":
            roll(D, command[1])
        if command[0] == "F":
            roll(F, command[1])
        if command[0] == "B":
            roll(B, command[1])
        if command[0] == "L":
            roll(L, command[1])
        if command[0] == "R":
            roll(R, command[1])
        '''
    
def roll(upperside, direction, U, D, F, B, L, R):
    
    if upperside == 'U':
        if direction == '+':
            temp = F[0][:]
            for i in range(3):
                F[0][i] = R[0][i]
                R[0][i] = B[0][i]
                B[0][i] = L[0][i]
            for i in range(3):
                L[0][i] = temp[i]
        else:
            temp = F[0][:]
            for i in range(3):
                F[0][i] = L[0][i]
                L[0][i] = B[0][i]
                B[0][i] = R[0][i]
            for i in range(3):
                R[0][i] = temp[i]
        rotate(U, direction)
    if upperside == 'D':
        if direction == '-':
            temp = F[2][:]
            for i in range(3):
                F[2][i] = R[2][i]
                R[2][i] = B[2][i]
                B[2][i] = L[2][i]
            for i in range(3):
                L[2][i] = temp[i]
        else:
            temp = F[0][:]
            for i in range(3):
                F[2][i] = L[2][i]
                L[2][i] = B[2][i]
                B[2][i] = R[2][i]
            for i in range(3):
                R[2][i] = temp[i]
        rotate(D, direction)
    
    if upperside == 'F':
        if direction == '+':
            temp = U[2][:]
            for i in range(3) :
                U[2][i] = L[2-i][2]
                L[2-i][2] = D[0][2-i]
                D[0][2-i] = R[i][0]
            for i in range(3) :
                R[i][20]= temp[i]
        else:
            temp = U[2][:]
            for i in range(3):
                U[2][i] = R[i][0]
                R[i][0] = D[0][2-i]
                D[0][2-i] = L[2-i][2]
            for i in range(3) :
                L[2-i][2] = temp[i]
        rotate(F, direction)
    
    if upperside == 'B':
        if direction == '-':
            temp = U[0][:]
            for i in range(3) :
                U[0][i] = L[2-i][0]
                L[2-i][0] = D[2][2-i]
                D[2][2-i] = R[i][2]
            for i in range(3) :
                R[i][2]= temp[i]
        else:
            temp = U[0][:]
            for i in range(3):
                U[0][i] = R[i][2]
                R[i][2] = D[2][2-i]
                D[2][2-i] = L[2-i][0]
            for i in range(3) :
                L[2-i][0] = temp[i]
        rotate(B, direction)
    
    if upperside == 'L':
        if direction == '+':
            temp= list(zip(*U))[0]
            for i in range(3) :
                U[i][0] = B[2-i][2]
                B[2-i][2] = D[i][0]
                D[i][0] = F[i][0]
            for i in range(3) :
                F[i][0]= temp[i]
        else:
            temp = list(zip(*U))[0]
            for i in range(3):
                U[i][0] = F[i][0]
                F[i][0] = D[i][0]
                D[i][0] = B[2-i][2]
            for i in range(3) :
                B[2-i][2] = temp[i]
        rotate(L, direction)
    if upperside == 'R':
        if direction == '-':
            temp= list(zip(*U))[2]
            for i in range(3) :
                U[i][2] = B[2-i][0]
                B[2-i][0] = D[i][2]
                D[i][2] = F[i][2]
            for i in range(3) :
                F[i][2]= temp[i]
        else:
            temp = list(zip(*U))[2]
            for i in range(3):
                U[i][2] = F[i][2]
                F[i][2] = D[i][2]
                D[i][2] = B[2-i][0]
            for i in range(3) :
                B[2-i][0] = temp[i]
        rotate(R, direction)





    

def rotate(side, direction):
    new_side = [[0]*3 for _ in range(3)]
    if direction == '+':
        for i in range(3):
            for j in range(3):
                new_side[j][2-i] = side[i][j]
    else:
        for i in range(3):
            for j in range(3):
                new_side[2-j][i] = side[i][j]
    for i in range(3):
        for j in range(3):
            side[i][j] = new_side[i][j]

for test_case in range(1,T+1):
    N = int(input())
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    cube = [[F, L, B, R], [R,B,L,F] ]
    command_list = list(input().split(' '))

    process_command(command_list, U, D, F, B, L, R)

    for i in range(3):
        print("".join(U[i]))



