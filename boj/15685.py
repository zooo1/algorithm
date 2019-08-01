import sys
input = sys.stdin.readline

def makeCurve(x, y, d, g):
    Q = []
    dragon[y][x] = 1
    Q.append([x,y]) 
    tx, ty = x+dx[d], y+dy[d]
    dragon[ty][tx] = 1
    Q.append([tx,ty]) 
    
    for i in range(g):
        endX, endY = Q[-1]
        idx = len(Q)-2
        while idx>=0:
            x, y = Q[idx]
            tx, ty = x-endX, y-endY
            ty, tx = -tx, ty
            ny, nx = endY-ty, endX-tx
            dragon[ny][nx] = 1
            Q.append([nx, ny])
            idx -= 1

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
N = int(input())
ans = 0
dragon = [[0]*101 for _ in range(101)]
for n in range(N):
    x, y, d, g = map(int, input().split())
    makeCurve(x, y, d, g)
for r in range(100):
    for c in range(100):
        if dragon[r][c] and dragon[r][c+1] and dragon[r+1][c] and dragon[r+1][c+1]:
            ans += 1
print(ans)
            