import sys
input = sys.stdin.readline
def moveDice(x, y, d):
    # 방향에 따라 주사위 위치가 변한다.
    tmp1, tmp2, tmp3, tmp4, tmp5, tmp6 = dice[1], dice[2], dice[3], dice[4], dice[5], dice[6]
    if d == 0:
        dice[1], dice[3], dice[4], dice[6] = tmp4, tmp1, tmp6, tmp3
    elif d == 1:
        dice[1], dice[3], dice[4], dice[6] = tmp3, tmp6, tmp1, tmp4
    elif d == 2:
        dice[1], dice[2], dice[5], dice[6] = tmp5, tmp1, tmp6, tmp2
    else:
        dice[1], dice[2], dice[5], dice[6] = tmp2, tmp6, tmp1, tmp5
        
def cmpDice(x, y):
    if board[x][y]:
        dice[6][1] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = dice[6][1]
    
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0 ]
N, M, x, y, K = map(int, input().split())
board = [ [int(x) for x in input().split()] for _ in range(N)]
orders = [int(x) for x in input().split()] 
dice = [[0,0] for _ in range(7)]

for order in orders:
    d = order-1
    if (0<=x+dx[d]<N and 0<=y+dy[d]<M):
        x += dx[d]
        y += dy[d]
        moveDice(x, y, d)
        cmpDice(x, y)
        print(dice[1][1])
