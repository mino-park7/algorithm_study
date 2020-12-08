import sys

sys.stdin = open("bj16234.txt", "r")

N, L, R = map(int, input().split())

A = [list(map(int, input().split()))for _ in range(N)]
def pprint(mat):
    for row in mat:
        print(row)
    print()
class Tree(object):
    def __init__(self, N):
        self.tree = [i for i in range(N*N)]
        self.N = N
        self.equilibrium = True
    '''
    def change_coor1(self, pos):
        return pos[0]*self.N+pos[1]
    def change_coor2(self, n):
        return (n//self.N, n%self.N)
    '''
    def find(self, pos1):
        #pos1 = pos[0]*self.N + pos[1]
        
        if pos1 == self.tree[pos1]:
            #return (pos1//self.N, pos1%self.N)
            return self.tree[pos1]
        else:
            #self.tree[pos1] = self.change_coor1(self.find(self.change_coor2(self.tree[pos1])))
            self.tree[pos1] = self.find(self.tree[pos1])
            return self.tree[pos1]

    def add(self,pos1, pos2):
        head_pos1 = self.find(pos1)
        head_pos2 = self.find(pos2)
        if head_pos2 == head_pos1:
            return
        #self.tree[self.change_coor1(pos2)] = self.change_coor1(pos1)
        self.tree[head_pos2] = head_pos1
        self.find(pos2)
        self.find(pos1)
        self.equilibrium = False

    def update(self):
        for i in range(self.N **2):
            self.find(i)

    def tree_init(self):
        self.__init__(self.N)

def is_fusion(y, x,tree:Tree):
    if y != N-1:
        if x== N-1:
            dx = [0]
            dy = [1]
        else:
            dx = [0,1]
            dy = [1,0]
    else:
        if x == N-1:
            dx = []
            dy = []
        else:
            dx = [1]
            dy = [0]
    
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        dist = abs(A[y][x] - A[ny][nx])
        if L<= dist<=R:
            tree.add(N*y+x, N*ny+nx)

my_tree = Tree(N)
my_tree.equilibrium = False
result = 0
#pprint(A)
while my_tree.equilibrium == False:
    my_tree.tree_init()
    for i in range(N):
        for j in range(N):
            is_fusion(i, j, my_tree)
    my_tree.update()
    
    #my_tree.update()
    fusion_list = []
    fusion_pos = {}
    for i, val in enumerate(my_tree.tree):
        if i != val and val not in fusion_list:
            fusion_list.append(val)
            fusion_pos[val] = []

    for i, val in enumerate(my_tree.tree):
        if val in fusion_list:
            fusion_pos[val].append(i)

    for pos_list in fusion_pos.values():
        mean_fusion = 0
        for pos in pos_list:
            mean_fusion += A[pos//N][pos%N]
        mean_fusion = mean_fusion // len(pos_list)
        for pos in pos_list:
            A[pos//N][pos%N] = mean_fusion
    if my_tree.equilibrium == False:
        result += 1
    #print(my_tree.tree)
    #pprint(A)
print(result)

        
