def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    
    def all_visited():
        for i in range(len(tickets)):
            if visited[i] == 0:
                return False
        return True

    def DFS(ans, idx, order):
        if all_visited():
            answer.append(ans[:])
            return
        
        else:
            for i in range(len(tickets)):
                if tickets[i][0] == ans[-1] and not visited[i]:
                    visited[i] = order
                    ans.append(tickets[i][1])
                    DFS(ans, i, order+1)
                    ans.pop()
                    visited[i] = 0

    tickets.sort(key=lambda x: (x[0], x[1]))
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            ans = tickets[i]
            visited[i] = 1
            DFS(ans, i, 2)
            visited[i] = 0

    return answer[0]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))