import sys
input = sys.stdin.readline
def check():
    # print(*ladder, sep="\n")
    # N: 세로, H:가로
    global N, H
    for c in range(N):
        r, tc, = 0, c
        while r<H:
            if ladder[r][tc] =='r':
                tc += 1
            elif ladder[r][tc] == 'l':
                tc -= 1
            r += 1
        if c!=tc:
            return False
    return True        
    

def find():
    global N, H
    # 0 개
    res = 0
    if check():
        return res
    # 1개
    if len(possible) == 0:
        return -1
    res += 1
    for i in range(len(possible)):
        r, c = possible[i]
        ladder[r][c] = 'r'
        ladder[r][c+1] = 'l'
        if check():
            return res
        ladder[r][c] = 0
        ladder[r][c+1] = 0
    # 2개
    if len(possible) == 1:
        return -1
    res += 1
    for i in range(len(possible)):
        r, c = possible[i]
        ladder[r][c] = 'r'
        ladder[r][c+1] = 'l'
        for j in range(i+1, len(possible)):
            rr, cc = possible[j]
            if ladder[rr][cc] == 0:
                ladder[rr][cc] = 'r'
                ladder[rr][cc+1] = 'l'
                if check():
                    return res
                ladder[rr][cc] = 0
                ladder[rr][cc+1] = 0
        ladder[r][c] = 0
        ladder[r][c+1] = 0

    # 3개
    if len(possible) == 2:
        return -1
    res += 1
    for i in range(len(possible)):
        r, c = possible[i]
        ladder[r][c] = 'r'
        ladder[r][c+1] = 'l'

        for j in range(i+1, len(possible)):
            rr, cc = possible[j]
            if ladder[rr][cc] == 0:
                ladder[rr][cc] = 'r'
                ladder[rr][cc+1] = 'l'
                for k in range(j+1, len(possible)):
                    rrr, ccc = possible[k]
                    if ladder[rrr][ccc] == 0:
                        ladder[rrr][ccc]= 'r'
                        ladder[rrr][ccc+1] = 'l'
                        if check():
                            return res
                        ladder[rrr][ccc] = 0
                        ladder[rrr][ccc+1] = 0
                ladder[rr][cc] = 0
                ladder[rr][cc+1] = 0
        ladder[r][c] = 0
        ladder[r][c+1] = 0

    return -1
    
    
    
# N:col, H:row
N, M, H = map(int, input().split())
ladder = [[0]*N for _ in range(H)]
possible = []

# ladder에 이미 있는 사다리 붙이기
for m in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    ladder[r][c] = 'r'
    ladder[r][c+1] = 'l'

# 가능한 
for r in range(H):
    for c in range(N):
        if ladder[r][c] == 0:
            if c+1<N and ladder[r][c+1] == 0:
                possible.append([r,c])

print(find())
            

