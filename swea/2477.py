def clear():
    for i in range(len(customerInfo)):
        if customerInfo[i][0] == -1 or customerInfo[i][1] == -1:
            return 0
    return 1

T = int(input())
for t in range(T):
    # 접수 창구의 개수, 정비 창구의 개수, 고객의 수, 고객이 두고간 접수, 정비 창구의 번호
    N, M, K, A, B = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    tk = [int(x) for x in input().split()]

    reception = [[] for _ in range(N)]
    repair = [[] for _ in range(M)]

    repairWaiting = []
    customerInfo = [[-1, -1] for _ in range(K)]

    time = 0
    while not clear():
        # 접수 창구
        for n in range(N):
            if reception[n]:
                reception[n][1] -= 1
                if reception[n][1] == 0:
                    repairWaiting.append(reception[n][0])
                    reception[n] = []

        for k in range(K):
            if time >= tk[k] and customerInfo[k][0] == -1:
                for n in range(N):
                    if not reception[n]:
                        reception[n] = [k, a[n]]
                        customerInfo[k][0] = n
                        break
        # 정비 창구
        # repair[0]: 고객 번호, [1]: 시간
        for m in range(M):
            if repair[m]:
                repair[m][1] -= 1
                if repair[m][1] == 0:
                    repair[m] = []

        for m in range(M):
            if not repair[m]:
                if repairWaiting:
                    customer = repairWaiting.pop(0)
                    repair[m] = [customer, b[m]]
                    customerInfo[customer][1] = m
        time += 1

    # 창구번호 확인하기
    ans = 0
    flag = 0
    for k in range(K):
        if customerInfo[k][0] == A-1 and customerInfo[k][1] == B-1:
            ans += k+1
            flag= 1

    if flag:
        print("#{} {}".format(t+1, ans))
    else:
        print("#{} {}".format(t+1, -1))





