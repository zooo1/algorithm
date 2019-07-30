# import sys
# sys.stdin = open("5656_input.txt", "r")
def findBrick(tmpBoard, col):
    global H
    for h in range(H):
        if tmpBoard[h][col]:
            return h
    # 벽돌이 없을 경우
    return -1

def cleanBoard(tmpBoard):
    global W, H
    # column마다 비교한다.
    for w in range(W):
        i = H-1
        while i>=0:
            if tmpBoard[i][w] == 0:
                j = i-1
                while j>=0:
                    if tmpBoard[j][w]:
                        tmpBoard[i][w] = tmpBoard[j][w]
                        tmpBoard[j][w] = 0
                        break
                    else:
                        j -= 1
            i -= 1

def cntBrick(tmpBoard):
    global W, H 
    cnt = 0
    for h in range(H):
        for w in range(W):
            if tmpBoard[h][w]:
                cnt += 1
    return cnt


def breakOut():
    global W, H, ans
    tmpBoard = [[0]*W for _ in range(H)]
    Q = set()
    # copy Board
    for h in range(H):
        for w in range(W):
            tmpBoard[h][w] = board[h][w]
    
    for idx in perm:
        height = findBrick(tmpBoard, idx)
        if height != -1:
            power = tmpBoard[height][idx]
            r, c = height, idx
            Q.add((r,c))
            
            while Q:
                r, c = Q.pop()
                power = tmpBoard[r][c]
                tmpBoard[r][c] = 0
                for i in range(4):
                    for p in range(1, power):
                        tr, tc = r+dr[i]*p, c+dc[i]*p

                        if(0<=tr<H and 0<=tc<W and tmpBoard[tr][tc]):
                            Q.add((tr,tc))
        cleanBoard(tmpBoard)
    leftBrick = cntBrick(tmpBoard)
    if leftBrick < ans:
        ans = leftBrick
def findMin(cnt):
    global N, W, H
    if cnt == N:
        breakOut()
        # 구슬깨기를 시작하자
    else:
        for i in range(W):
            perm[cnt] = i
            findMin(cnt+1)
            perm[cnt] = 0


        
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
T = int(input())
for t in range(T):
    N, W, H = map(int, input().split())
    board = [[int(x) for x in input().split()]for _ in range(H)]
    perm = [0] * N
    ans = 0xffffff
    findMin(0)
    
    print("#{} {}".format(t+1, ans))
