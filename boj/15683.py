import sys
input = sys.stdin.readline

def find(idx, n, Q):
    global N, M, ans
    if idx == n:
        # 계산하기
        res = calc(Q)
        if ans>res:
            ans = res
        return 
    else:
        r, c, num = cctv[idx]
        if num == 2:
            for i in range(2):
                Q.append([r,c,num,i])
                find(idx+1, n, Q)
                Q.remove([r,c,num,i])
        elif num == 5:
            Q.append([r,c, num, 0])
            find(idx+1, n, Q)
            Q.remove([r,c,num,0])
        else:
            for i in range(4):
                Q.append([r,c,num,i])
                find(idx+1, n, Q)
                Q.remove([r,c,num,i])

def calc(Q):
    global N, M, wall
    watch = set()
    length = len(Q)
    Qidx = 0
    while Qidx<length:  
        r, c, num, idx = Q[Qidx]
        if num == 1:
            tr, tc = r, c
            while (0<=tr<N and 0<=tc<M):
                if office[tr][tc] == 0:
                    watch.add((tr,tc))
                elif office[tr][tc] == 6:
                    break
                tr, tc = tr+dr[idx], tc+dc[idx]

        elif num == 2:
            for i in range(idx, 4, 2):
                tr, tc = r, c
                while (0<=tr<N and 0<=tc<M):
                    if office[tr][tc] == 0:
                        watch.add((tr,tc))
                    elif office[tr][tc] == 6:
                        break
                    tr, tc = tr+dr[i], tc+dc[i]

        elif num == 3:
            for i in [idx, (idx+1)%4]:
                tr, tc = r, c 
                while (0<=tr<N and 0<=tc<M):
                    if office[tr][tc] == 0:
                        watch.add((tr,tc))
                    elif office[tr][tc] == 6:
                        break
                    tr, tc = tr+dr[i], tc+dc[i]

        elif num == 4:
            for i in [idx, (idx+1)%4, (idx+2)%4 ]:
                tr, tc = r, c
                while (0<=tr<N and 0<=tc<M):
                    if office[tr][tc] == 0:
                        watch.add((tr,tc))
                    elif office[tr][tc] == 6:
                        break  
                    tr, tc = tr+dr[i], tc+dc[i]
          
        if num == 5:
            for i in range(4):
                tr, tc = r, c
                while (0<=tr<N and 0<=tc<M):
                    if office[tr][tc] == 0:
                        watch.add((tr,tc))
                    elif office[tr][tc] == 6:
                        break
                    tr, tc = tr+dr[i], tc+dc[i]
        Qidx += 1

    return (N*M - wall - len(cctv) - len(watch))

# 북 서 남 동(0,1,2,3)
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
N, M = map(int, input().split())
office = [[int(x) for x in input().split()] for _ in range(N)]
cctv = []
wall = 0

for r in range(N):
    for c in range(M):
        if (1<=office[r][c]<=5):
            cctv.append([r,c,office[r][c]])
        elif office[r][c] == 6:
            wall += 1

ans = N * M - len(cctv) - wall
find(0, len(cctv), [])
print(ans)
