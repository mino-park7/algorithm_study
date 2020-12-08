import sys
#from itertools import combinations
sys.stdin = open("bj15686.txt", "r")

N, M  = map(int, input().split())

def comb(my_list:list, N):
    q = []
    if N == 1:
        for li in my_list:
            yield [li]
    else:
        for li in my_list[::-1]:
            q.append(([li]))
        while q:
            visited = q.pop()
            for li in my_list[::-1]:
                if li not in visited:
                    new_visit = visited + [li]
                    if len(new_visit) == N:
                        yield new_visit
                    else:
                        q.append(new_visit)

chicken_map = [[0]*N for _ in range(N)]
chicken = []
house = []
for i in range(N):
    for j, val in enumerate(map(int,input().split())):
        chicken_map[i][j] = val
        if val == 1:
            house.append((i,j))
        if val == 2:
            chicken.append((i,j))
def calc_dist(pos1, pos2):
    result = 0
    for i in range(2):
        result += abs(pos1[i]-pos2[i])
    return result

smallest = [[{} for _ in range(N)]for _ in range(N)]

for i in range(N):
    for j in range(N):
        if chicken_map[i][j] == 1:
            for k in chicken:
                temp = calc_dist((i,j), k)
                try:
                    smallest[i][j][temp].append(k)
                except:
                    smallest[i][j][temp] = []
                    smallest[i][j][temp].append(k)
              

#print(smallest)

result = 987654321

for chik in comb(chicken, M):
    sub_result = 0
    for i in range(N):
        for j in range(N):
            if chicken_map[i][j] == 1:
                for dist, poss in sorted(smallest[i][j].items()):
                    is_break = 0
                    for pos in poss:
                        if pos in chik:
                            sub_result += dist
                            is_break = 1
                            break
                    if is_break==1:
                        break
    
    if sub_result < result:
        result = sub_result

print(result)

