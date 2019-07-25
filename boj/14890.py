import sys
input = sys.stdin.readline

def makeSlope(n):
    global N, L
    slope = [0]*N
    i, j = 0,0 
    while(i<N-1):
        # 다음 index와 같은 값
        if (board[n][i] == board[n][i+1]):
            i += 1
        # 다음 index에서 높이가 1 클 때 
        elif (board[n][i] +1 == board[n][i+1]):
            j = i
            cnt = 0
            while (j>=0 and cnt<L):
                if (not slope[j] and board[n][j]+1==board[n][i+1]):
                    j -= 1
                    cnt += 1
                else:
                    return 0

            if cnt == L:
                for k in range(j+1, i+1):
                    slope[k] = 1 
                i += 1
            else: 
                return 0
        # 다음 index에서 높이가 1 작을 때 
        elif(board[n][i]-1 == board[n][i+1]):
            j = i+1
            cnt = 0
            while (j<N and cnt<L):
                if (not slope[j] and board[n][j] == board[n][i]-1):
                   j += 1
                   cnt += 1
                else:
                    return 0
            if cnt == L:
                for k in range(i+1, j):
                    slope[k] = 1 
                i = j-1       
            else:
                return 0
        # 나머지 경우는 모두 불가능함
        else:
            return 0
    return 1



N, L = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
ans = 0

for n in range(N):
    ans += makeSlope(n)
board = list(zip(*board))
for n in range(N):
    ans += makeSlope(n)
print(ans)

