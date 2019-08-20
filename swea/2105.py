# import sys
# sys.stdin = open("2105_input.txt", "r")
dr, dc = [1,1, -1, -1], [1, -1, -1, 1]

# 간단한 DFS 문제
def find(start, r, c, cnt, d):
    global ans, N

    if start == (r, c):
        if cnt > ans:
            ans = cnt
        return

    else:
        # 그 방향 그대로
        tr, tc =  r+dr[d], c+dc[d]
        if 0<=tr<N and 0<=tc<N and not check[cafe[tr][tc]]:
            check[cafe[tr][tc]] = 1
            find(start, tr, tc, cnt+1, d)
            check[cafe[tr][tc]] = 0
        # 방향을 바꾼다.
        if d+1< 4:
            d+= 1
            nr, nc =  r+dr[d], c+dc[d]
            if d < 4 and 0<=nr<N and 0<=nc<N and not check[cafe[nr][nc]]:
                check[cafe[nr][nc]]  = 1
                find(start, nr, nc, cnt+1, d)
                check[cafe[nr][nc]] = 0

T = int(input())
for t in range(T):
    N = int(input())
    cafe = [[int(x) for x in input().split()] for _ in range(N)]
    ans = -1
    for r in range(N):
        for c in range(N):
            check = [0] * 101
            start = (r, c)
            d = 0
            tr, tc = r+dr[d], c+dc[d]
            if 0<=tr<N and 0<=tc< N and not check[cafe[tr][tc]]:
                check[cafe[tr][tc]] = 1
                find(start, tr, tc, 1, d)
                check[cafe[tr][tc]] = 0
    print("#{} {}".format(t+1, ans))




