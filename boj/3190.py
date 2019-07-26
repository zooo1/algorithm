import sys
input = sys.stdin.readline
dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
def game():
    global N 

    # 초기 값  
    # d: 방향 
    d = 3
    r, c = 0, 0
    head = [r,c]
    tail = [r,c]
    board[r][c] = d
    # 꼬리 위치를 바꿀 때 방향이 필요하다. 

    # 뱀의 모양을 보여주자!
    board[r][c] = d
    time = 0
    # print(*board, sep="\n")
    # print()
    while 1:
        time += 1
        # 뱀의 이동 
        tr, tc = r+dr[d], c+dc[d]
        # print(f"tr, tc => {tr, tc}")
        if dInfo and time==dInfo[0][0]:
            # print("방향을 바꿔주자")
            sec, switchD = dInfo.pop(0)
            # D: 왼족
            if switchD == "L":
                d = (d+1)%4
            else:
                d = (d-1)%4
            # board[r][c] = d

        if(0<=tr<N and 0<=tc<N):
            # 사과가 있는경우
            if (board[tr][tc] == '*'):
                # print("사과를 먹는다.")
                r, c = tr, tc
                head = [r,c]
                board[r][c] = d
            
            # 자신을 만남 -> 주금
            elif(0<=board[tr][tc]<4):
                # print("죽음 자신을 만났음")
                return time

            # 아무것도 없는 경우 -> 꼬리와 머리의 위치 변경
            elif(board[tr][tc]==-1):
                # print("뱀 이동!")
                # 1. 꼬리 이동
                tailR, tailC = tail
                # print(f"현재 꼬리 위치: {tailR, tailC}")
                tailD = board[tailR][tailC]
                tail = [tailR+dr[tailD], tailC+dc[tailD]]
                # print(f"이동할 꼬리 위치: {tail[0], tail[1]}")
                board[tailR][tailC] = -1
                # 2. 머리 이동
                r, c = tr, tc
                board[r][c] = d
                head= [r, c]
        else:
            # print("벽에 부딪힘")
            return time
        # 방향 바꿔주기 - 방향 전환 정보는 X 증가하는 순으로 주어짐
                           
        #     print(f"옮겨질 방향: {d}")
        # print(*board, sep="\n")
        # print()

# N: 보드 크기
# K: 사과 개수
N = int(input())
K = int(input())
board = [[-1]*N for _ in range(N)]
dInfo = []
for k in range(K):
    # 사과는 보드에서 *로 표시한다.
    r, c = map(int, input().split())
    board[r-1][c-1] = '*'  

L = int(input())

for l in range(L):
    # 초, 방향
    t, d = input().split()
    t = int(t)
    dInfo.append([t, d])

ans = 0
# 게임이 끝나는 조건:
# 벽과 부딪히거나 자신의 몸과 부딪히는 경우
print(game())


