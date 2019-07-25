from itertools import combinations
import sys
input = sys.stdin.readline

def calcSynergy(startTeam, linkTeam):
    global ans
    startSum = 0
    linkSum = 0
    startPair = combinations(startTeam, 2)
    linkPair = combinations(linkTeam, 2)
    for members in startPair:
        x, y = members
        startSum += power[x][y] + power[y][x]

    for members in linkPair:
        x, y = members
        linkSum += power[x][y] + power[y][x]
    
    if abs(startSum-linkSum) < ans:
        ans = abs(startSum-linkSum)

N = int(input())
power = [[int(x) for x in input().split()] for _ in range(N)]

teams = combinations(range(N), N//2)
ans = 0xffffff
i = 0
for team in teams:
    print(team)
    i += 1
    startTeam = []
    linkTeam = []
    for member in team:
        startTeam.append(member)
    for n in range(N):
        if n not in startTeam:
            linkTeam.append(n)
    calcSynergy(startTeam, linkTeam)
print(i)
print(ans)
