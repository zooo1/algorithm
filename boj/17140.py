import sys
input = sys.stdin.readline

def rowIsBigger():
    return len(A)>=len(A[0])

def sortA():
    R, C = len(A), len(A[0])

    # 개수 세기
    for r in range(R):
        cnt = []
        for c in range(C):
            flag = 0
            num = A[r][c]
            if num == 0:
                continue
            length = len(cnt)
            for i in range(length):
                if cnt[i][1] == num:
                    cnt[i][0] += 1
                    flag = 1
                    break
            if flag == 0:
                cnt.append([1, num])
        cnt.sort()
        A[r] = []
        while cnt:
            c, num = cnt.pop(0)
            A[r].extend([num, c])

    # 가장 긴 배열 찾기
    maxLen = 0
    for r in range(R):
        if maxLen<len(A[r]):
            maxLen = len(A[r])
    
    # 가장 긴 배열 길이에 맞춰 0을 붙여주기
    for r in range(R):
        if maxLen> len(A[r]):
            A[r].extend([0]*(maxLen-len(A[r])))



r, c, k = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(3)]
ans = 0
while ans <= 100:

    if r-1<len(A) and c-1<len(A[0]) and A[r-1][c-1] == k:
        break
    elif rowIsBigger():
        sortA()
    else:
        A = list(zip(*A))
        sortA()
        A = list(zip(*A))
    ans += 1

if ans >100:
    print(-1)
else:
    print(ans)

