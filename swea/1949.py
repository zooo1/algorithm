# import sys
# sys.stdin = open('sample_input (2).txt', 'r')


def find(x, y, cnt):
    global flag, N, K, Max
    visited[x][y] = 1

    if cnt > Max:
        Max = cnt
    for i in range(4):
        tx, ty = x+dx[i], y+dy[i]
        if (0<=tx<N and 0<=ty<N) and not visited[tx][ty]:
            if Map[tx][ty] < Map[x][y]:
                find(tx, ty, cnt+1)
                visited[tx][ty] = 0

            else:
                # 아직 깎은 적이 없다면 가능
                if flag:
                    for k in range(1, K+1):
                        if Map[tx][ty] - k < Map[x][y]:
                            flag = 0
                            Map[tx][ty] = Map[tx][ty] - k

                            find(tx, ty, cnt+1)
                            visited[tx][ty] = 0
                            Map[tx][ty] = Map[tx][ty] + k
                            flag = 1



TC = int(input())
dx, dy = [1,-1,0,0], [0,0,1,-1]
for tc in range(TC):
    N, K = map(int, input().split())
    Map = [[int(x) for x in input().split()] for _ in range(N)]
    MaxHeight = 1
    Max = 1
    start = []
    visited = [[0]*N for _ in range(N)]
    flag = 1
    # 등산로 중 가장 높은 곳의 높이를 찾아내기
    for i in range(N):
        for j in range(N):
            if Map[i][j] > MaxHeight:
                MaxHeight = Map[i][j]

    # 가장 높은 봉우리를 찾기
    for i in range(N):
        for j in range(N):
            if Map[i][j] == MaxHeight:
                start.append([i,j])

    for i in range(len(start)):
        find(start[i][0], start[i][1], 1)
        visited[start[i][0]][start[i][1]] = 0

    print(f'#{tc+1} {Max}')