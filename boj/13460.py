import sys
from collections import deque
# sys.stdin = open("13460_input.txt", "r")

input =sys.stdin.readline
TC= 26
def findMin():
    global ans, N, M
    Q = deque()
    Q.append([RED, BLUE, 0])

    while Q:
        direction = set()
        red, blue, cnt = Q.popleft()
        if cnt >= 10:
            return -1
        else:
            rx, ry, bx, by = red[0], red[1], blue[0], blue[1]

            # 방향 설정 
            for i in range(4):
                nrx, nry = rx+dx[i], ry+dy[i]
                nbx, nby = bx+dx[i], by+dy[i]
                # 빨간색, 파란색 구슬 따로 확인한다.
                if (board[nrx][nry]!='#'):
                    direction.add(i) 
                if (board[nbx][nby]!='#'):
                    direction.add(i)
            # print(direction)


            # 각 방향마다 움직여준다.
            for d in direction:
                # print(f"방향 : {d}")
                # print(f"현재 red, blue의 위치: {rx, ry},  {bx, by}")
                rGoal = False
                bGoal = False
                
                # 빨강 -> 파랑 -> 빨강
                tRx, tRy =  rx, ry
                while 1:
                    if (tRx == HOLE[0] and tRy == HOLE[1]):
                        rGoal = True
                        break
                    elif (board[tRx][tRy] == '#' or (tRx==bx and tRy==by)):
                        tRx -= dx[d]
                        tRy -= dy[d]
                        break
                    else:
                        tRx += dx[d]
                        tRy += dy[d]
                # red = [tRx, tRy]
    
                
                # 파란색 옮겨주기
                tBx, tBy = bx, by
                while 1:
                    if(tBx==HOLE[0] and tBy==HOLE[1]):
                        bGoal = True
                        break

                    elif(board[tBx][tBy] == '#' or (tBx == tRx and tBy==tRy)):
                        tBx -= dx[d]
                        tBy -= dy[d]
                        break
                    else:
                        tBx += dx[d]
                        tBy += dy[d]
                blue = [tBx, tBy] 
    
                while 1:
                    if (tRx == HOLE[0] and tRy == HOLE[1]):
                        rGoal = True
                        break
                    elif (board[tRx][tRy] == '#' or (tRx==tBx and tRy==tBy)):
                        tRx -= dx[d]
                        tRy -= dy[d]
                        break
                    else:
                        tRx += dx[d]
                        tRy += dy[d]

                red = [tRx, tRy]
    

                if bGoal == False:
                    if rGoal:
                        return cnt+1
                    else:
                        # print(f"다음위치 red:{red}   blue: {blue} 움직인 횟수: {cnt+1}")
                        Q.append([red, blue, cnt+1])


         
    return -1

# 북, 서, 남, 동

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
# for t in range(TC):
N, M = map(int, input().split())
board = [input() for _ in range(N)]
ans = 0

# red, blue 위치 찾기
for r in range(N):
    for c in range(M):
        if board[r][c] == 'B':
            BLUE = [r,c]
        if board[r][c] == 'R':
            RED = [r,c]
        if board[r][c] == 'O':
            HOLE = [r,c]
print(findMin())
