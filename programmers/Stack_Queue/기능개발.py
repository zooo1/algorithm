import math 

def solution(progresses, speeds):
    visited = [0] * len(progresses)
    answer = []
    for i in range(len(progresses)):
        if not visited[i]:
            visited[i] = 1
            day = math.ceil((100 - progresses[i]) / speeds[i])
            j = i + 1
            while j < len(progresses):
                if progresses[j] + speeds[j] * day < 100:
                    break
                else:
                    visited[j] = 1
                    j += 1
            answer.append(j-i)    
    return answer

print(solution( [40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))