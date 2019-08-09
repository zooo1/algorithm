<<<<<<< HEAD
def check():
    global D, W, K
    for c in range(W):
        flag = film[0][c]
        available = False
        r = 1
        while r<D:
            cnt = 0
            for k in range(K):
                if cnt == K:
                    available = True
                    break
                if r+k>=D:
                    r += k 
                    break
                
                else:
                    r += 1
                    flag = abs(flag-1)
                    break       
            if available:
                break

        if not available:
=======
# import sys
from itertools import combinations
# sys.stdin = open("2112_input.txt", "r")

def check(film):
    global D, W
    # column 중 하나라도 K개의 연속되는 특성이 없으면 return 0
    for c in range(W):
        r = 0
        POSSIBLE = 0
        while r<D:
            flag = film[r][c]
            cnt = 0
            for k in range(1, K):
                if r+k<D and film[r+k][c] == flag:
                    cnt += 1
                else:
                    r += k
                    break
            if cnt == K-1:
                POSSIBLE = 1
                break
        if POSSIBLE == 0:
>>>>>>> a8c2b0680681ca8adfe2c0bca6e358b2191d3070
            return 0
    return 1


<<<<<<< HEAD


def makePermutation(idx, cnt):
    global D, W, ans
    print(*film,sep="\n")
    print()
    if idx >=D:
        return 
    # if check():
    #     if ans > cnt:
    #         ans = cnt
    #         return

    for i in range(idx, D):
        tmp = film[i]
        # 투입 x
        makePermutation(i+1, cnt)
        # 투입 A
        film[i] = [0] * W
        makePermutation(i+1, cnt+1)
        film[i] = tmp
        # 투입 B
        film[i] = [1] * W
        makePermutation(i+1, cnt+1)
        film[i] = tmp

        
T = int(input())
for t in range(T):
    D, W, K = map(int, input().split())
    film = [[int(x) for x in input().split()] for _ in range(D)]
    ans = D
    makePermutation(0,0)
    # if check():
    #     print("#{} 0".format(t+1))
    # else:
    #     pass
# 1. 순열 만들기
=======
def changeFilm(comb, k, cnt, copied):
    global W, D, FOUND
    if cnt == k:
        if check(copied):
            FOUND = 1
        return 
    else:
        # A
        copied[comb[k]] = [0] * W
        changeFilm(comb, k+1, cnt, copied)
        # B
        copied[comb[k]] = [1] * W
        changeFilm(comb, k+1, cnt, copied)

        
def resetFilm(comb, copied):
    for c in comb:
        copied[c] = film[c][:]

def findMin(cnt):
    global D, W, FOUND
    copied = [0] * D
    for d in range(D):
        copied[d] = film[d][:]
    combs = combinations(list(range(D)), cnt)
    for comb in combs:
        changeFilm(comb, 0, cnt, copied)
        if FOUND:
            return 1
        else:
            resetFilm(comb, copied)
    return 0


for t in range(int(input())):
    D, W, K = map(int, input().split())
    film = [[int(x) for x in input().split()] for _ in range(D)]
    FOUND = 0
    if K == 1 or check(film):
        print("#{} 0".format(t+1))
    else:
        for ans in range(1, K+1):
            if findMin(ans):
                print("#{} {}".format(t+1, ans))
                break
>>>>>>> a8c2b0680681ca8adfe2c0bca6e358b2191d3070
