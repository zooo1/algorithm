def make_perm(k, N, order):
    # if k >= N:
    #     print(order)
    if all_checked(order):
        print(order) 

    else:
        for i in range(N):
            if order[i] == -1:
                order[i] = k
                make_perm(k+1, N, order)


def all_checked(order):
    for i in range(len(order)):
        if order[i] == -1:
            return False
    return True


def solution(numbers):
    N = len(numbers)
    for i in range(N):
        make_perm(0, N, [-1]*N)
    answer = ''
    return answer


solution([6, 10, 2])