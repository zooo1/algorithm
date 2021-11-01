def solution(enter, leave):
    N = len(enter)
    answer = dict()
    orders = dict()
    result = [0 for _ in range(N)]

    for i in range(1, N + 1):
        answer[i] = set()
        orders[i] = dict()
        orders[i]['enter'] = enter.index(i)
        orders[i]['leave'] = leave.index(i)
    
    for x_idx in range(N):
        x = enter[x_idx]
        for y_idx in range(x_idx + 1, N):
            y = enter[y_idx]
            if orders[x]["enter"] < orders[y]["enter"]:
                if orders[x]["leave"] > orders[y]["leave"]:
                    answer[x].add(y)
                    answer[y].add(x)
                else:
                    rest_enter_set = set(enter[y_idx + 1: ])
                    rest_leave_set = set(leave[0 : orders[x]["leave"]])
                    if len(rest_enter_set.intersection(rest_leave_set)) > 0 :
                        answer[x].add(y)
                        answer[y].add(x)

    for key, value in answer.items():
        result[key-1] = len(value)
    return result
    

print(solution([1,3,2], [1,2,3]))
print(solution([1,4,2,3], [2,1,3,4]))
print(solution([3,2,1], [2,1,3]))
print(solution([3,2,1], [1,3,2]))
print(solution([1,4,2,3], [2,1,4,3]))

print(solution([1, 2, 3], [1, 2, 3])) # [0, 0, 0]
print(solution([1, 2, 3], [3, 2, 1])) # 
print(solution( [1, 2, 3, 4], [3, 4, 2, 1]))
print(solution( [1, 2, 3, 4], [4, 2, 1, 3]))
print(solution( [1, 2, 3, 4, 5], [5, 3, 1, 2, 4]))
print(solution( [1, 4, 5, 3, 2], [5, 4, 3, 2, 1]))
print(solution([1, 3, 2, 4, 6, 5, 8, 7, 9, 10], [9, 5, 1, 10, 7, 4, 8, 6, 2, 3]))
print(solution( [1, 10, 9, 2, 3, 8, 7, 4, 5, 6], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))