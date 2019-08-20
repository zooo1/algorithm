import sys
input = sys.stdin.readline
dr, dc = [-1,0,1,0], [0,1,0,-1]
R, C, T = map(int, input().split())
room = [[int(x) for x in input().split()] for _ in range(R)]

def spread():
    global R, C
    while microDust:
        r, c, density = microDust.pop(0)
        spreadQ = []
        cnt = 0
        for i in range(4):
            tr, tc = r+dr[i], c+dc[i]
            if (0<=tr<R and 0<=tc<C and room[tr][tc]!= -1):
                cnt += 1
                spreadQ.append([tr,tc])
        
        while spreadQ:
            tr, tc = spreadQ.pop(0)
            room[tr][tc] += density//5
        room[r][c] = room[r][c] - (density//5)*cnt

def clean():
    global R, C
    up, down = airCleaner

    # 1. 위부터
    r, c = up
    rr, cc = r-1, c
    d = 0

    # 0열
    while rr>0:
        rrr, ccc = rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc
    # 0행
    d += 1
    while cc<C-1:
        rrr, ccc =rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc
    # c-1열
    d += 1
    while rr<r:
        rrr, ccc= rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc
    d += 1
    while cc>c+1:
        rrr, ccc = rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc =rrr, ccc
    room[rr][cc] = 0

    # 2. down
    r, c = down
    rr, cc = r+1, c
    d = 2
    # 0열
    while rr<R-1:
        rrr, ccc = rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc    
    
    d = (d-1)%4
    while cc<C-1:
        rrr, ccc =rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc

    d = (d-1)%4
    while rr>r:
        rrr, ccc= rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc = rrr, ccc                    

    d = (d-1)%4
    while cc>c+1:
        rrr, ccc = rr+dr[d], cc+dc[d]
        room[rr][cc] = room[rrr][ccc]
        rr, cc =rrr, ccc
    room[rr][cc] = 0


def calcMicrodustDensity():
    global R, C
    res = 0
    for r in range(R):
        for c in range(C):
            if room[r][c] != -1 and room[r][c] != 0:
                res += room[r][c]
    return res

for t in range(T):
    airCleaner = []
    microDust = []
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                airCleaner.append([r,c])
            elif room[r][c]:
                microDust.append([r,c, room[r][c]])
    spread()
    clean()
print(calcMicrodustDensity())
            
