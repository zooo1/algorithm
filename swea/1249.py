from collections import deque
dr, dc = [-1, 0, 1, 0] , [0, -1, 0, 1]
def findMin():
    global N, ans
    visited = [[0xffffff]*N for _ in range(N)]
    Q = deque()
    Q.append((0,0,0))
    visited[0][0] = 1
    while Q:
        r, c, height = Q.popleft()
        for i in range(4):
            tr, tc = r+dr[i], c+dc[i]
            if (0<=tr<N and 0<=tc<N):
                if (tr==N-1 and tc==N-1 and ans>height):
                    ans = height
                elif visited[tr][tc] > height+board[tr][tc]:
                    visited[tr][tc] = height + board[tr][tc]
                    Q.append( (tr,tc, height+board[tr][tc] ))
T = int(input())
for t in range(T):
    N = int(input())
    board = [[int(x) for x in input().replace('', ' ').split()] for _ in range(N)]
    ans = 0xffffff
    findMin()
    print("#{} {}".format(t+1, ans))