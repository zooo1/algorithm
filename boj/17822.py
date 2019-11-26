import sys
input = sys.stdin.readline

# 원판 돌리기
def turn_plate():
    global X, D, K, N, M
    i = 1
    x = X
    while x <= N:
        # 시계 방향
        if D == 0:
            for _ in range(K):
                tmp = board[x][:-1]
                board[x] = [board[x][-1]]
                board[x].extend(tmp)      
        # 반시계 방향
        else:
            for _ in range(K):
                tmp = board[x][0]
                board[x] = board[x][1:]
                board[x].append(tmp)          
        i += 1
        x = X * i
    

# 인접하면서 수가 같은 것 모두 찾기
def check_same_num():
    global N, M
    flag = 0
    numerator, denominator = 0, 0 

    check = [[0 for _ in range(M)] for _ in range(N+1)]
    for r in range(1, N+1):
        for c in range(M):
            if board[r][c] != 'x':
                # 오른쪽
                numerator += board[r][c]
                denominator += 1
                if c == 0 and board[r][c] == board[r][M-1]:
                    flag = 1
                    check[r][c] = check[r][M-1] = 1
                if 0<=c+1<M and board[r][c] == board[r][c+1]:
                    flag = 1
                    check[r][c] = check[r][c+1] = 1
                if 0<=r+1<=N and board[r][c] == board[r+1][c]:
                    flag = 1
                    check[r][c] = check[r+1][c] = 1

    if flag:
        for r in range(1, N+1):
            for c in range(M):
                if check[r][c]:
                    board[r][c] = 'x'

    elif flag == 0 and denominator:
        avg = numerator / denominator
        for r in range(1, N+1):
            for c in range(M):
                if board[r][c] != 'x':
                    if board[r][c] > avg:
                        board[r][c] -= 1
                    elif board[r][c] < avg:
                        board[r][c] += 1
    

if __name__ == "__main__":
    N, M, T = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N+1)] 

    for n in range(1, N+1):
        board[n] = [int(x) for x in input().split()]

    for t in range(T):
        X, D, K = map(int, input().split())
        turn_plate()
        check_same_num()

    ans = 0
    for n in range(1, N+1):
        for m in range(M):
            if board[n][m] != 'x':
                ans += board[n][m]

    print(ans)
    
