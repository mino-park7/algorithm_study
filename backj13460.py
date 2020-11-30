import sys
from collections import deque
sys.stdin = open('backj13460.txt','r')
direc = [(1,0), (-1,0), (0,-1), (0,1)]
def pprint(list_2d):
    """
    docstring
    """
    for li in list_2d:
        print(li)

def move(direction, rp:list, bp:list, board_to_move):
    """
    input:
        direction : 0 = up, 1 = down, 2 = left, 3 = right 
    """
    
    #position = rp

    def _moveBall(position, color):
        """
        docstring
        """
        if board[position[0]][position[1]] ==  'O':
            return
        
        #board[position[0]][position[1]] = '.'
        while True:
            new_position = board[position[0]+direc[direction][0]][position[1]+direc[direction][1]]
            if  new_position != ".":
                if new_position  == 'O':
                    position[0] += direc[direction][0]
                    position[1] += direc[direction][1]
                    return
                break
            else:
                position[0] += direc[direction][0]
                position[1] += direc[direction][1]
        

        board[position[0]][position[1]] = color
        

    if direction == 0 or direction == 1:
        if rp[1] == bp[1]:
            if direction == 0:
                if rp[0] < bp[0]:
                    _moveBall(rp, 'R')
                    _moveBall(bp, 'B')
                else:
                    _moveBall(bp, 'B')
                    _moveBall(rp, 'R')
            else:
                if rp[0] < bp[0]:
                    _moveBall(bp, 'B')
                    _moveBall(rp, 'R')
                else:
                    _moveBall(rp, 'R')
                    _moveBall(bp, 'B')
        else:
            _moveBall(rp, 'R')
            _moveBall(bp, 'B')
    else:
        if rp[0] == bp[0]:
            if direction == 2:
                if rp[1] < bp[1]:
                    _moveBall(rp, 'R')
                    _moveBall(bp, 'B')
                else:
                    _moveBall(bp, 'B')
                    _moveBall(rp, 'R')
            else:
                if rp[1] < bp[1]:
                    _moveBall(bp, 'B')
                    _moveBall(rp, 'R')
                else:
                    _moveBall(rp, 'R')
                    _moveBall(bp, 'B')
        else:
            _moveBall(rp, 'R')
            _moveBall(bp, 'B')
    pprint(board)
    print(' ')
    if board[rp[0]][rp[1]] != 'O':
        board[rp[0]][rp[1]] = '.'
    if board[bp[0]][bp[1]] != 'O':
        board[bp[0]][bp[1]] = '.'

def is_move(direction, rp, bp):
    """
    docstring
    """
    trp = [v + direc[direction][i] for i,v in enumerate(rp)]
    tbp = [v + direc[direction][i] for i,v in enumerate(bp)]
    '''
    nrp = board[rp[0]+direc[direction][0]][rp[1]+direc[direction][1]]
    nbp = board[bp[0]+direc[direction][0]][bp[1]+direc[direction][1]]
    '''
    
    if board[trp[0]][trp[1]] == '.' or board[trp[0]][trp[1]] == 'O':
        rlt_rp = True
    else:
        rlt_rp = False
    if board[tbp[0]][tbp[1]] == 'O' or board[tbp[0]][tbp[1]] == '.' :
        rlt_bp = True
    else:
        rlt_bp = False
    if rp == tbp :
        rlt_bp = False
    if bp == trp :
        rlt_rp = False

    return rlt_rp or rlt_bp
        
def dfs(rp, bp):
    """
    docstring
    """
    q = deque()
    result = 11
    for i in range(4):
        if is_move(i, rp, bp):
            q.append((rp, bp, i,1))
    while q:
        trp, tbp, direct, step = q.pop()
        nrp = trp[:]
        nbp = tbp[:]
        if step > result or step > 10:
            continue
        
        move(direct, nrp, nbp, board)
        if board[nbp[0]][nbp[1]] == 'O' :
            continue
        if board[nrp[0]][nrp[1]] == 'O'  :
            if result >= step :
                result = step
        else:
            for i in range(4):
                if is_move(i, nrp, nbp):
                    q.append((nrp, nbp, i, step+1))

    if result > 10:
        result = -1
    return result 


if __name__ == "__main__":
    N, M = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    #pprint(board)
    #print(' ')
    rp = list([(i,j) for i in range(N) for j in range(M) if board[i][j]=='R'][0])
    bp = list([(i,j) for i in range(N) for j in range(M) if board[i][j]=='B'][0])
    board[rp[0]][rp[1]] = '.'
    board[bp[0]][bp[1]] = '.'
    #move(3, rp, bp, board)

    #pprint(board)
    result = dfs(rp, bp)

    print(result)
