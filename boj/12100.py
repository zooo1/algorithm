# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록 -> 그 전에 더 큰 수의 블록이 생길 수도 있다? 
import sys
input = sys.stdin.readline
def copyBoard(tmpBoard, board):
    global N
    for r in range(N):
        for c in range(N):
            tmpBoard[r][c] = board[r][c]
            
def game(board, cnt):
    global N, ans
    maxNum = 0
    if cnt == 5:
        # 가장 큰 블록을 출력한다.
        for r in range(N):
            for c in range(N):
                if board[r][c] > maxNum:
                    maxNum = board[r][c]
        if maxNum > ans:
            ans = maxNum
    else:

        # boardCopy -> 각 방향으로 움직인 후 game에 다시 보내기
        # 상
        tmpBoard = [[0]*N for _ in range(N)]
        copyBoard(tmpBoard, board)
        check = [[0]*N for _ in range(N)]
        for c in range(N):
            for r in range(N):
                i, j = r, c
                value = tmpBoard[r][c]
                # 한 칸씩 옮겨준다.
                while i>=0:
                    # 현재로부터 한 칸 위가 0 일 때 -
                    if (i-1>=0 and tmpBoard[i-1][j] == 0):
                        tmpBoard[i][j] = 0
                        tmpBoard[i-1][j] = value
                        i -= 1
                    elif(i-1>=0 and tmpBoard[i-1][j] != 0):
                        if (tmpBoard[i-1][j] == tmpBoard[i][j] and not check[i-1][j]):
                            check[i-1][j] = 1
                            tmpBoard[i-1][j] *= 2
                            tmpBoard[i][j] = 0
                        else:
                            tmpBoard[r][c] = 0
                            tmpBoard[i][j] = value
                        break
                    elif i-1<0:
                        tmpBoard[r][c] = 0
                        tmpBoard[i][j] =value
                        break
        game(tmpBoard, cnt+1)
        
        # 하
        tmpBoard = [[0]*N for _ in range(N)]
        copyBoard(tmpBoard, board)
        check = [[0]*N for _ in range(N)]
        for c in range(N):
            for r in range(N-1, -1, -1):
                i, j = r, c
                value = tmpBoard[r][c]
                # 한 칸씩 옮겨준다.
                while i<N:
                    # 현재로부터 한 칸 아래가 0 일 때 -
                    if (i+1<N and tmpBoard[i+1][j] == 0):
                        tmpBoard[i][j] = 0
                        tmpBoard[i+1][j] = value
                        i += 1
                    elif(i+1<N and tmpBoard[i+1][j] != 0):
                        if (tmpBoard[i+1][j] == tmpBoard[i][j] and not check[i+1][j]):
                            check[i+1][j] = 1
                            tmpBoard[i+1][j] *= 2
                            tmpBoard[i][j] = 0
                        else:
                            tmpBoard[r][c] = 0
                            tmpBoard[i][j] = value
                        break
                    elif i+1>=N:
                        tmpBoard[r][c] = 0
                        tmpBoard[i][j] =value
                        break
        game(tmpBoard, cnt+1)

        
        # 좌
        tmpBoard = [[0]*N for _ in range(N)]
        copyBoard(tmpBoard, board)
        check = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                i, j = r, c
                value = tmpBoard[r][c]
                # 한 칸씩 옮겨준다.
                while j>=0:
                    # 현재로부터 한 칸 위가 0 일 때 -
                    if (j-1>=0 and tmpBoard[i][j-1] == 0):
                        tmpBoard[i][j] = 0
                        tmpBoard[i][j-1] = value
                        j -= 1
                    elif(j-1>=0 and tmpBoard[i][j-1] != 0):
                        if (tmpBoard[i][j-1] == tmpBoard[i][j] and not check[i][j-1]):
                            check[i][j-1] = 1
                            tmpBoard[i][j-1] *= 2
                            tmpBoard[i][j] = 0
                        else:
                            tmpBoard[r][c] = 0 
                            tmpBoard[i][j] = value
                        break
                    elif j-1<0:
                        tmpBoard[r][c] = 0
                        tmpBoard[i][j] =value
                        break
        game(tmpBoard, cnt+1)

        # 우
        tmpBoard = [[0]*N for _ in range(N)]
        copyBoard(tmpBoard, board)
        check = [[0]*N for _ in range(N)]
        for r in range(N):
            for c in range(N-1, -1, -1):
                i, j = r, c
                value = tmpBoard[r][c]
                # 한 칸씩 옮겨준다.
                while j<N:
                    # 현재로부터 한 칸 아래가 0 일 때 -
                    if (j+1<N and tmpBoard[i][j+1] == 0):
                        tmpBoard[i][j] = 0
                        tmpBoard[i][j+1] = value
                        j += 1
                    elif(j+1<N and tmpBoard[i][j+1] != 0):
                        if (tmpBoard[i][j+1] == tmpBoard[i][j] and not check[i][j+1]):
                            check[i][j+1] = 1
                            tmpBoard[i][j+1] *= 2
                            tmpBoard[i][j] = 0
                        else:
                            tmpBoard[r][c] = 0
                            tmpBoard[i][j] = value
                        break
                    elif j+1>=N:
                        tmpBoard[r][c] = 0
                        tmpBoard[i][j] =value
                        break
        game(tmpBoard, cnt+1)


N= int(input())
board = [[int(x) for x in input().split()] for _ in range(N)]
ans = 0
game(board, 0)
print(ans)