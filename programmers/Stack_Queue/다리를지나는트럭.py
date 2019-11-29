def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = []
    truck_idx = 0

    while 1:
        if truck_idx >= len(truck_weights) and len(stack) <= 0 :
            break
        if len(stack):
            if stack[0][1] >= bridge_length-1:
                stack.pop(0)
            for i in range(len(stack)):
                stack[i][1] += 1
        if len(stack) < bridge_length and truck_idx < len(truck_weights):
            w = 0
            for i in range(len(stack)):
                w += stack[i][0]
            if w + truck_weights[truck_idx] <= weight:
                stack.append([truck_weights[truck_idx], 0])
                truck_idx += 1

        answer += 1    
    return answer

# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))