def solution(array, commands):
    answer = []
    while commands:
        i, j, k = commands.pop(0)
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer
