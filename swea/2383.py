# import sys
# sys.stdin = open("2383_input.txt", "r")

def makeComb(k, L, idx):
    if k == L:
        move()

    else:
        for i in range(idx, L):
            for j in range(2):
                people[k][2] = j
                makeComb(k+1, L, i+1) 


def move():
    # people 0: 0계단까지의 거리 1:1계단까지의 거리 2: 선택한 계단
    global L, ans
    time = 0
    stairs = [ [0,0,0] for _ in range(2)]
    # 모두 내려갔는지 확인하기
    # 0: 아직 안내려감 1: 내려가고 있는 중 2: 다 내려감
    check = [0] * L
    while notAllCheck(check):
        time += 1
        # 계단 내려가기
        for i in range(2):
            for j in range(3):
                if stairs[i][j] != 0:  
                    stairs[i][j][1] -= 1
                    if stairs[i][j][1] <= 0:
                        check[stairs[i][j][0]] = 2
                        stairs[i][j] = 0              
                     
        # 계단까지 이동하기
        for i in range(L):
            pick = people[i][2]   
            if people[i][pick] <= time and check[i] == 0:
                for j in range(3):
                    if stairs[pick][j] == 0:
                        stairs[pick][j] = [i, stairHeight[pick]]
                        check[i] = 1
                        break
    if time < ans:
        ans = time

def notAllCheck(check):
    global L
    for i in range(L):
        if check[i] != 2:
            return 1
    return 0

T = int(input())
for t in range(T):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]
    people = []
    stairPosition = []
    stairHeight = []
    ans = 0xffffff

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                people.append([r,c,0])
            elif board[r][c] >= 2:
                stairPosition.append([r,c])
                stairHeight.append(board[r][c])
    
    # 각 거리 구하기
    L = len(people)

    for i in range(L):
        r, c, s = people[i]
        for j in range(2):
            people[i][j] = abs(r-stairPosition[j][0]) + abs(c-stairPosition[j][1])
    makeComb(0, L, 0)
    print("#{} {}".format(t+1, ans+1))

