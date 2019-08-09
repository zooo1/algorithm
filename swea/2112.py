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
            return 0
    return 1




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