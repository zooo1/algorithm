def solution(n, wires):
    answer = n
    tree = [ [] for _ in range(n + 1)]

    def check_nodes(num, new_tree):
        for new_num in tree[num]:
            if not visited[new_num]:
                visited[new_num] = 1
                new_tree.append(new_num)
                check_nodes(new_num, new_tree)

    for wire in wires:
        a = wire[0]
        b = wire[1]
        tree[a].append(b)
        tree[b].append(a)
    
    for wire in wires:
        visited = [0 for _ in range(n + 1)]
        a = wire[0]
        b = wire[1]
        treeA = [a]
        treeB = [b]
        visited[a] = 1
        visited[b] = 1
        check_nodes(a, treeA)
        check_nodes(b, treeB)
        answer = min(abs(len(treeA) - len(treeB)), answer)

    return answer


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,	[[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	))