import sys
from itertools import combinations
import time
now = time.time()
#input = sys.stdin.readline
sys.stdin = open("bj14889.txt", "r")

N = int(input())

def calc_power(team_list):
    power = 0
    for member in team_list:
        for other_member in team_list:
            if member != other_member:
                power += power_mat[member][other_member]
    return power



def select_team(N):
    member_N = int(N/2)

    comb = combinations(list(range(N)), member_N)

    result = float('inf')

    for c in comb:
        sum1 = calc_power(c)
        sum2 = calc_power(list(set(list(range(N))) - set(c)))

        if result > abs(sum1-sum2):
            result = abs(sum1-sum2)
    
    return result



power_mat = [list(map(int, input().split())) for _ in range(N)]

#print(select_team(N))
print(list(zip(*power_mat))[1])
print(time.time() - now)
