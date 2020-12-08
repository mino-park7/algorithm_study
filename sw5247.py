import sys
#from heapq import heappush, heappop
sys.stdin = open("sw5247.txt", "r")

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        curr_node = Node(data)
        if self.length == 0:
            self.head = curr_node
            self.tail = curr_node
        else:
            self.tail.next = curr_node
            self.tail = curr_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        curr_node = self.head
        self.head = curr_node.next
        self.length -= 1
        data = curr_node.data
        curr_node = None
        return data

    def final(self):
        while self.length !=0:
            _=self.pop()

def bfs(s,e):
    q = SingleLinkedList()
    q.append((s,0))
    visited = [False]* 1000001
    visited[s] = True
    while q.length != 0:
        m, count = q.pop()
        count += 1
        for i in range(4):
            n_m = 0
            '''
            if m < e:
                if i == 1 or i == 3:
                    continue
            else:
                if i == 0 or i == 2:
                    continue
            '''
            if i == 0:
                n_m = m+1
            elif i == 1:
                n_m = m- 1
            elif i == 2:
                n_m = m*2     
            else:
                n_m = m-10
            
            if 0 <= m <= 1000000:
                if n_m == e:
                    q.final()
                    return count
                elif visited[n_m] == False:
                    q.append((n_m,count))
                    visited[n_m] = True
            else:
                continue

def my_calc(num, i):
    if i == 0:
        return num + 1
    elif i == 1:
        return num * 2
    elif i == 2:
        return num - 1
    elif i == 3:
        return num - 10
    else:
        return 0


def BFS(N, M):
    dq = SingleLinkedList()
    dq.append((N,0))
    #states = ['+1', '*2', '-1', '-10']
    #print(result)
    while dq.length != 0:
        num, count = dq.pop()
        if num == M :
            
            result = count
            return result
        for state in range(4):
            num2 = my_calc(num, state)
            #print(num2)
            if 0 <= num2 <= 1000000 and visited[num2] != test_case :
                dq.append((num2, count+1))
                #print(dq)
                visited[num2]=test_case
                
    
    
    
    
    
T = int(input())
visited = [0] * 1000001
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    
    
    N, M = map(int,input().split())
    #result = 0
    #print(result)
    
    #print(dq)
    result = BFS(N, M)
    print("#%i %i"%(test_case,result))
    # ///////////////////////////////////////////////////////////////////////////////////
