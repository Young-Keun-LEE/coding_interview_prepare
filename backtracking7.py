import sys, itertools
def backtrack(start_team, index):
    global min_val
    
    if len(start_team) == N / 2:
        link_team = [i for i in range(1, N + 1) if i not in start_team]
        start_team_ability = 0
        link_team_ability = 0

        for i, j in itertools.combinations(start_team, 2):
            start_team_ability += ability[i - 1][j - 1] + ability[j - 1][i - 1]
    
        for i, j in itertools.combinations(link_team, 2):
            link_team_ability += ability[i - 1][j - 1] + ability[j - 1][i - 1]

        min_val = min(min_val,abs(start_team_ability - link_team_ability))

        return

    for player in range(index + 1, N + 1):
        start_team.append(player)
        backtrack(start_team, player)
        start_team.pop()
        

input = sys.stdin.readline
N = int(input()) # Abilty is N * N matrix
ability = []
min_val = int(1e9)
start_team = []


for _ in range(N):
    ability.append(list(map(int, input().split())))

backtrack(start_team, 0)
print(min_val)



