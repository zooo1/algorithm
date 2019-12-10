def solution(n, edge):
    G = [[] for _ in range(n+1)]
    dist = [0] * (n+1)

    def visit(cnt, v):
        Q = [(v, cnt)]
        dist[v] = cnt
        while Q:
            Node, cnt = Q.pop(0)
            for w in G[Node]:
                if not dist[w]:
                    dist[w] = cnt+1
                    Q.append((w, cnt+1))

    for a, b in edge:
        G[a].append(b)
        G[b].append(a)
    
    visit(1, 1)

    return dist.count(max(dist))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))