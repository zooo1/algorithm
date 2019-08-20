import sys
from collections import deque
input = sys.stdin.readline
N = 10
def findMin(idx):
    global ans, FOUND
    
    if idx >= len(Q):
        FOUND = 1
        res = 30-sum(coloredPaper)
        if res<ans:
            print(coloredPaper)
            # print(*visited, sep="\n")
            # print()
            ans = res 
        
    else:
        r, c = Q[idx]
        if visited[r][c]:
            findMin(idx+1)
        else:
            # 사이즈 1~5까지 체크한다. (dfs)
            for s in range(1,6):
                # print("r, c: {} {}".format(r, c))
                # print("size: {}".format(s))
                # print()
                if coloredPaper[s]-1<0:
                    return

                for i in range(s):
                    for j in range(s):
                        if r+i<N and c+j<N and board[r+i][c+j]:
                            continue
                        else:
                            return 

                # visited 처리
                for i in range(s):
                    for j in range(s):
                        visited[r+i][c+j] = 1
                # 색종이 종이 수 줄여주기
                coloredPaper[s] -= 1
                findMin(idx+1)
                coloredPaper[s] += 1
                # visited 해제
                for i in range(s):
                    for j in range(s):
                        visited[r+i][c+j] = 0

board = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[0]*N for _ in range(N)]
coloredPaper = [5] * 6
FOUND = 0
ans = 0xfffff
Q = deque()
for r in range(N):
    for c in range(N):
        if board[r][c]:
            Q.append((r,c))

findMin(0)
if FOUND:
    print(ans)
else:
    print(-1)


