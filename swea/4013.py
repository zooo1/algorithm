SIZE = 4

def checkRotatable(check, magNum, d):
    left = magNum -1
    right = magNum +1
    
    l, r = magNum, magNum
    direction = d
    while left>=0:
        if check[l] and magnetics[left][2] != magnetics[l][6]:
            direction = -direction
            check[left] = direction
            l = left
            left -= 1
        else:
            break

    direction = d
    while right<SIZE:
        if check[r] and magnetics[r][2] != magnetics[right][6]:
            direction = -direction
            check[right] = direction
            right += 1
            r += 1
        else:
            break
    

def rotate(magNum, d):
    check = [0]*SIZE
    check[magNum] = d
    # 각 자석들이 움직일 수 있는지 확인하기
    checkRotatable(check, magNum, d)

    # 자석 회전
    for i in range(SIZE):
        if check[i] == 1:
            tmp = magnetics[i][-1] 
            magnetics[i]= [tmp] + magnetics[i][:7]

        elif check[i] == -1:
            tmp = magnetics[i][0]
            magnetics[i] = magnetics[i][1:] + [tmp]

def getScore():
    score = 0
    for s in range(SIZE):
        score += magnetics[s][0] * (2**s)
    return score


for t in range(int(input())):
    K = int(input())
    magnetics = [[int(x) for x in input().split()] for _ in range(SIZE)]

    for k in range(K):
        # magNum : 자석의 번호, d: 방향(-1: 반시계, 1: 시계)
        magNum, d = map(int, input().split())
        # 회전
        rotate(magNum-1, d)

    
    print("#{} {}".format(t+1, getScore()))