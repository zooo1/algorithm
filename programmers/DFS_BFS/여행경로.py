def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    remove_name = []
    for i in range(len(tickets)):
        for j in range(i+1, len(tickets)):
            if tickets[i][0] == tickets[j][0] and tickets[i][1] == tickets[j][1]:
                remove_name.append(tickets[i])
    while remove_name:
        name = remove_name.pop()
        tickets.remove(name)
    
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
                    ans.remove(tickets[i][1])
                    visited[i] = 0

    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            ans = tickets[i]
            visited[i] = 1
            DFS(ans, i, 2)
            visited[i] = 0

    return sorted(answer)

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution([ [ "ICN", "COO"], [ "COO", "ICN"], [ "COO", "ICN" ] ]))
a = [[ "ICN", "COO"], [ "COO", "ICN"], [ "COO", "ICN" ] ]
