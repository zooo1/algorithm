import sys
from collections import deque
input = sys.stdin.readline
Q = deque()

direction = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

def not_all_visited(visited):
    global M, N, H
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato_info[h][n][m] == 0 and not visited[h][n][m]:
                    return 1
    return 0


def BFS():
    global M, N, H 
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    while Q:
        h, n, m, day = Q.popleft()
        # print(h, n, m, day)
        for d in direction:
            test_h, test_n, test_m = h+d[0], n+d[1], m+d[2]
            if 0<=test_h<H and 0<=test_n<N and 0<=test_m<M and tomato_info[test_h][test_n][test_m] == 0 and not visited[test_h][test_n][test_m]:
                visited[test_h][test_n][test_m] = 1
                Q.append((test_h, test_n, test_m, day+1))
    
    return -1 if not_all_visited(visited) else day


def init():
    empty_cnt = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato_info[h][n][m] == 1:
                    Q.append((h, n, m, 0))
                elif tomato_info[h][n][m] == -1:
                    empty_cnt += 1

    if M*N*H - empty_cnt == len(Q):
        return 0
    
    elif M*N*H - empty_cnt == M*N*H - len(Q):
        return -1

    else:
        return 1


M, N, H = map(int, input().split())  # column, row, height
tomato_info = [[[int(x) for x in input().split()] for _ in range(N)] for _ in range(H)]

start = init()
if start == 1:
    print(BFS())
else:
    print(start)