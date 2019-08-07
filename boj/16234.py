import sys
input = sys.stdin.readline

def canMakeUnion():
    global N
    idx = -1
    for r in range(N):
        for c in range(N):
            if not check[r][c]:
                # bfs
                idx += 1
                check[r][c] = 1
                Q[idx].append([r,c])
                j = 0

                while 1:
                    if j >= len(Q[idx]):
                        break
                    tr, tc = Q[idx][j]
                    for k in range(4):
                        nr, nc = tr+dr[k], tc+dc[k]
                        if 0<=nr<N and 0<=nc<N and not check[nr][nc]:
                            if (L<=abs(people[tr][tc]-people[nr][nc])<=R):
                                check[nr][nc] = 1
                                Q[idx].append([nr, nc])
                    j += 1
    if idx==N*N-1:
        return 0
    return 1
    
def movePeople():
    i = 0
    # 계산 
    while Q[i]:
        Sum = 0
        # 이동 인구 수를 구해주기
        for j in range(len(Q[i])):
            Sum += people[Q[i][j][0]][Q[i][j][1]]
        res = Sum // len(Q[i])
        for j in range(len(Q[i])):
            x, y = Q[i][j]
            people[x][y] = res
        i += 1

# 좌, 상, 우, 하
dr, dc = [0,-1,0,1], [-1,0,1,0]
N, L, R = map(int, input().split())
people = [[int(x) for x in input().split()] for _ in range(N)]
ans = 0

while 1:
    check = [[0]*N for _ in range(N)]
    Q = [[] for _ in range(2500)]
    if canMakeUnion():
        movePeople()    
        ans += 1
    else:
        break
print(ans)