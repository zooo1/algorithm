import sys
input = sys.stdin.readline
dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]

def findPlace(cnt):
    global r, c, d
    if cnt == 4:
        return 0
    else:
        tr, tc = r+dr[d], c+dc[d]
        if(board[tr][tc]==0 and not cleaned[tr][tc]):
            r, c = tr, tc
            if(d==0):
                d = 3
            else:
                d -= 1
            return 1
        else:
            if(d==0):
                d = 3
            else:
                d -= 1
            return findPlace(cnt+1)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
cleaned = [[0]*M for _ in range(N)]
ans = 0
flag = 0

while 1:
    # 현재 위치를 청소한다.
    ans += 1
    cleaned[r][c] = 1
    while 1:      
        flag = 0
        #네 방향 모두 청소가 되어있거나 벽인 경우
      
        if (findPlace(0)==0):
            br, bc = r+ (1-d)*((d-1)%2), c+ (d-2)*((d-2)%2)
            # 후진이 불가능하면 -> 끝냄
            if(board[br][bc]==1):
                flag = 1
                break
            # 후진이 가능하면 방향을 유지한 채로 한 칸 후진
            # 2번으로 돌아간다. (현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색 진행)
            else:
                r, c = br, bc
        else:
            break

    if flag:
        break

print(ans)

