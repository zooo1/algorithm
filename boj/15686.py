import sys
input = sys.stdin.readline

def makeChickenStreet():
    global N, M, ans
    distSum = 0
    for r, c in house:
        mindist = 0xffffff
        for rr, cc in combs:
            dist = abs(rr-r) + abs(cc-c)
            if mindist > dist:
                mindist = dist
        distSum += mindist
        if distSum > ans:
            return

    if ans > distSum:
        ans = distSum


def chooseChickenHouse(M, cnt, idx):
    if cnt == M:
        makeChickenStreet()
        return
    else:
        for i in range(idx, len(chicken)):
            combs[cnt] = chicken[i]
            chooseChickenHouse(M, cnt+1, i+1)
            combs[cnt] = 0

N, M = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]


chicken = []
house = []
combs = [0] * M
ans = 0xffffff

# 치킨집, 가정집의 위치를 찾는다
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            house.append([r, c])
        elif board[r][c] == 2:
            chicken.append([r, c])


chooseChickenHouse(M, 0, 0)
print(ans)


