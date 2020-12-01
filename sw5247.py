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

T = int(input())

for test_case in range(1,T+1):
    start, end = map(int, input().split())

    result = bfs(start, end)
    
    print("#%i %i"%(test_case,result))