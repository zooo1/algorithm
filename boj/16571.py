import sys
input = sys.stdin.readline
SIZE = 3

def all_visited():
    for i in range(len(visited)):
        if visited[i] == 0:
            return 0
    return 1


def DFS(cnt, turn, now_board):
    global SIZE, TURN
    copied_board = [now_board[x][:] for x in range(SIZE)]
    
    if cnt >= 9:

        return

    flag = 1
    # 1. 현재 내가 이길 수 있는가?
    for i in range(len(Q)):
        r, c = Q[i]
        if not visited[i]:
            visited[i] = 1
            copied_board[r][c] = turn
            # print(r, c)
            # print(*copied_board, sep='\n')
            # print()
            if TURN == find_winner(copied_board):
                # print(cnt)
                # print(*copied_board, sep='\n')
                # print()
                flag = 0
                SCORE.append((cnt, 'W'))
                return 
            visited[i] = 0
            copied_board[r][c] = 0


    
    # 2. 현재 내가 이길 수 없는 경우
    # 내가 이 곳에 두었을 때 다음 턴에서 상대방이 말을 두어 이긴다면 여기에 두면 안된다.
    # 내가 이 곳에 두었을 때 다음 턴에서 상대방이 말을 두어 비긴다면 여기에 두어도 된다. 

    if flag:
        for i in range(len(Q)):
            if not visited[i]:  
                r, c = Q[i]
                visited[i] = 1
                rival = 1 if turn == 2 else 2 
                copied_board[r][c] = turn
                if i_lose_next_step(copied_board, rival):
                    continue
                else:
                    DFS(cnt+1, rival, copied_board)
                copied_board[r][c] = 0
                visited[i] = 0


def i_lose_next_step(copied_board, rival):
    for i in range(len(Q)):
        if not visited[i]:
            visited[i] = 1
            r, c = Q[i]
            copied_board[r][c] = rival
            if rival == find_winner(copied_board):
                visited[i] = 0
                copied_board[r][c] = 0
                return 1
            visited[i] = 0
            copied_board[r][c] = 0
    return 1
            
            

def find_winner(copied_board):
    
    global SIZE
    ##  1. row
    for r in range(SIZE):
        x_cnt, o_cnt = 0, 0
        for c in range(SIZE):
            if copied_board[r][c] == 1:
                x_cnt += 1
            elif copied_board[r][c] == 2:
                o_cnt += 1

        if x_cnt >= SIZE:
            return 1
        if o_cnt >= SIZE:
            return 2
    
    ## 2. col
    for c in range(SIZE):
        x_cnt, o_cnt = 0, 0
        for r in range(SIZE):
            if copied_board[r][c] == 1:
                x_cnt += 1
            elif copied_board[r][c] == 2:
                o_cnt += 1

        if x_cnt >= SIZE:
            return 1
        if o_cnt >= SIZE:
            return 2
        
    ## 3. diag
    if copied_board[0][0] == 1 and copied_board[1][1] == 1 and  copied_board[2][2] == 1:
        return 1
    if copied_board[0][2] == 1 and copied_board[1][1] == 1 and  copied_board[2][0] == 1:
        return 1
    if copied_board[0][0] == 2 and copied_board[1][1] == 2 and  copied_board[2][2] == 2:
        return 2
    if copied_board[0][2] == 2 and copied_board[1][1] == 2 and  copied_board[2][0] == 2:
        return 2

    return 0   


'''
input
'''
board = [[int(x) for x in input().split()] for _ in range(SIZE)]
Q = []
SCORE = []
x_cnt, o_cnt = 0, 0
for r in range(SIZE):
    for c in range(SIZE):
        if board[r][c] == 0:
            Q.append((r, c))
        elif board[r][c] == 1:
            x_cnt += 1
        else:
            o_cnt += 1


TURN = 1 if x_cnt<=o_cnt else  2
visited = [0] * len(Q)
DFS(0, TURN, board)
SCORE.sort()

flag = 1

if not SCORE:
    print('L')
    flag = 0
else:
    for i in range(len(SCORE)):
        if SCORE[i][0] != 'D':
            print(SCORE[i][1])
            flag = 0
            break
if flag:
    print('D')