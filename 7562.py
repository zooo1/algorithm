import sys
input = sys.stdin.readline
from collections import deque

dr, dc = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
T = int(input())
for _ in range(T):
    I = int(input())
    r, c = map(int, input().split())
    goalR, goalC = map(int, input().split())
    visited =[[0]*I for _ in range(I)]

    if r==goalR and c==goalC:
        ans = 0
    else:
        Q = deque()
        visited[r][c] = 1
        Q.append([r, c, 0])
        flag = 0
        while Q:
            r, c, time = Q.popleft()
            for i in range(8):
                tr, tc = r+dr[i], c+dc[i]
                if (0<=tr<I and 0<=tc<I and not visited[tr][tc]):
                    if tr==goalR and tc==goalC:
                        flag = 1
                        ans = time+1
                        break
                    else:
                        visited[tr][tc] = 1
                        Q.append([tr,tc,time+1])  
            if flag:
                break     
    print(ans)