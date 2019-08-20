# 1. 순열 만들기
# 2. 배열 돌리기
# 3. 계산하기
import sys
input = sys.stdin.readline
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def makePermutation(cnt, K):
    global N
    if cnt == K:
        # copy board
        copied = [0] * N
        for r in range(N):
            copied[r] = board[r][:]
        # 배열 돌리기
        rotate(copied)

    else:
        for i in range(K):
            if not check[i]:
                perm[cnt] = i
                check[i] = 1
                makePermutation(cnt+1, K)
                check[i] = 0

def rotate(copied):
    global N, M, K, ans

    for k in range(K):
        r, c, s = info[perm[k]]
        start = [r-s-1, c-s-1]
        end = [r+s-1, c+s-1]
        lenR, lenC = end[0]-start[0]+1, end[1]-start[1]+1
        d = 0
        tmpR, tmpC = start
        tmp = copied[tmpR][tmpC]

        while lenR > 1 or lenC > 1:
            nr, nc = tmpR+dr[d], tmpC+dc[d]

            if not (start[0] <= nr <= end[0] and start[1] <= nc <= end[1]):
                d += 1
                nr, nc = tmpR+dr[d], tmpC+dc[d]

            tmpN = copied[nr][nc]
            copied[nr][nc] = tmp
            tmp = tmpN
            tmpR, tmpC = nr, nc

            # 한 바퀴 다 돈 경우
            if nr == start[0] and nc == start[1]:
                d = 0
                lenR -= 2
                lenC -= 2

                start = [start[0]+1, start[1]+1]
                end = [end[0]-1, end[1]-1]
                tmpR, tmpC = start[0], start[1]
                tmp = copied[tmpR][tmpC]


    # 최소 행을 찾는다.
    res = findMin(copied)
    if res < ans:
        ans = res

def findMin(copied):
    global N
    res = 0xfffff
    for r in range(N):
        Sum = sum(copied[r])
        if Sum < res:
            res = Sum
    return res

N, M, K = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
info = []
ans = 0xfffff
for k in range(K):
    info.append(list(map(int, input().split())))

for k in range(K):
    perm = [0] * K
    check = [0] * K
    perm[0] = k
    check[k] = 1
    makePermutation(1, K)
print(ans)