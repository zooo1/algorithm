import sys
input = sys.stdin.readline
dr, dc = [0, -1, 0], [-1, 0, 1]

def makeComb(SIZE, k, idx):
    global N, M
    if k == SIZE:
        defense()
    else:
        for i in range(idx+1, M):
            archers[k] = i
            makeComb(SIZE, k+1, i)

def defense():
    global N, M, D, ans
    # 1. copy
    res = 0
    tmpCastle = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tmpCastle[i][j] = castle[i][j]
    for n in range(N):
        enemies = set()
        for archer in archers:
            visited = [[0]*M for _ in range(N)]
            enemyCandidate = []
            Q = []
            archerR, archerC = N-n, archer
            Q.append([archerR, archerC])
            while Q:
                r, c = Q.pop(0)
                for i in range(3):
                    tr, tc = r+dr[i], c+dc[i]  
                    if (0<=tr<archerR and 0<=tc<M and not visited[tr][tc]):
                        if tmpCastle[tr][tc] ==  1:
                        # if tmpCastle[tr][tc] == 1 and (tr,tc) not in enemies:
                            # 거리, 방향(x축, y축) 
                            visited[tr][tc] = 1
                            enemyCandidate.append([abs(tr-archerR)+abs(tc-archerC), tc, tr])
                        else:
                            if abs(tr-archerR) + abs(tc-archerC) < D :
                                visited[tr][tc] = 1
                                Q.append([tr,tc])
            if enemyCandidate:
                enemyCandidate.sort()
                enemies.add((enemyCandidate[0][2],enemyCandidate[0][1]))
        res += killEnemy(enemies, tmpCastle)
    if ans < res:
        ans = res

def killEnemy(enemies, tmpCastle):
    res = 0
    for enemy in enemies:
        r, c = enemy
        tmpCastle[r][c] = 0             
        res += 1
    return res

N, M, D = map(int, input().split())
castle = [[int(x) for x in input().split()] for _ in range(N)]
archers = [0] * 3
ans = 0

for i in range(M-2):
    archers[0] = i
    makeComb(3, 1, i)
print(ans)