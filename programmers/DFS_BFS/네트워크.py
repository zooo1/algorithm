def solution(n, computers):
    visited = [0] * n

    def check(v):
        visited[v] = 1
        for w in range(n):
            if computers[v][w] and not visited[w]:
                check(w)

    answer = 0  
    for i in range(n):
        print("i", i, visited)
        if not visited[i]:
            visited[i] = 1
            answer += 1
            for v in range(n):
                if computers[i][v]:
                    check(v)

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
