from collections import deque

def BFS(start, end):
    global N
    visited = [0] * (N+1)
    Q = deque()
    Q.append((start, 0))
    visited[start] = 1
    while Q:
        now, cnt = Q.popleft()
        visited[now] = 1
        for num in G[now]:
            if not visited[num]:
                if num == end:
                    return cnt+1
                Q.append((num, cnt+1))


N, M = map(int, input().split())
min_num = 100000
ans = 0
G = [[] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N+1):
    Sum = 0
    for j in range(1, N+1):
        if i != j:
            Sum += BFS(i, j)
    if Sum < min_num:
        min_num = Sum
        ans = i

print(ans)