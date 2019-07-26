# 1. 시간초과
import sys
input = sys.stdin.readline

# 총 8개의 인접한 땅
dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
def spring():
    tmpQ = []
    # trees.sort()
    length = len(trees)
        
    while trees:
        r, c, age = trees.pop(0)
        if land[r][c] >= age:    
            land[r][c] -= age 
            age += 1
            if age % 5 == 0:
                birth.append([r, c])
            tmpQ.append([r, c, age])
        else:
            deadTrees.append([r,c,age])
    trees.extend(tmpQ)

def summer():
    while deadTrees:
        r, c, age = deadTrees.pop(0)
        land[r][c] += age//2

def fall():
    global N, M, K
    while birth:
        r, c = birth.pop(0)
        for i in range(8):
            tr, tc = r+dr[i], c+dc[i]
            # 땅을 벗어나는 칸에는 나무가 생기지 않는다.
            if (0<=tr<N and 0<=tc<N):
                trees.insert(0, [tr, tc, 1])
    
def winter():
    global N
    for r in range(N):
        for c in range(N):
            land[r][c] += A[r][c]

N, M, K = map(int, input().split())

A = [[int(x) for x in input().split()] for _ in range(N)]
trees = []
deadTrees = []
birth = []
land = [[5]*N for _ in range(N)]

# 초기 나무의 정보
for m in range(M):
    r, c, age = map(int, input().split())
    trees.append([r-1, c-1, age])

year = 0
while year < K:
    year += 1
    spring()
    summer()
    fall()
    winter() 

print(len(trees))

# 2. 정답
import sys
N, M, K = map(int, input().split())

# tree[r][c][0] => r,c 칸의 영양 정보
# tree[r][c][1] => r,c 칸에 심은 나무 정보
def springNSummer():
    global N
    for r in range(N):
        for c in range(N):
            DIE = 0

            for i in range(len(tree[r][c][1])):
                if (0< tree[r][c][1][i] <= tree[r][c][0]):
                    tree[r][c][0] -= tree[r][c][1][i]
                    tree[r][c][1][i] += 1
                elif (tree[r][c][1][i] == 0):
                    continue
                else:
                    DIE = 1
                    idx = i
                    break
            # 양분을 먹지 못하고 죽음s
            
            if DIE:
                for j in range(idx, len(tree[r][c][1])):
                    tree[r][c][0] += tree[r][c][1][j] // 2
                tree[r][c][1] = tree[r][c][1][:idx]

 
def fallNWinter():
    global N
    for r in range(N):
        for c in range(N):
            for i in range(len(tree[r][c][1])):
                if (tree[r][c][1][i] != 0 and  tree[r][c][1][i] % 5 ==0):
                    # 번식
                    for j in range(8):
                        tr, tc = r+dr[j], c+dc[j]
                        if(0<=tr<N and 0<=tc<N):
                            tree[tr][tc][1].insert(0, 1)

            tree[r][c][0] += A[r][c]



dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
A = [[int(x) for x in input().split()] for _ in range(N)]
tree = [[[5, []] for _ in range(N) ] for _ in range(N)]
ans = 0

# 나무의 초기 정보
for m in range(M):
    r, c, age = map(int, input().split())
    tree[r-1][c-1][1].append(age)

year = 0 
while year<K:
    year += 1
    springNSummer()
    fallNWinter()
    # print(*tree, sep="\n")
    # 결과 값 찾기
for r in range(N):
    for c in range(N):
        for i in range(len(tree[r][c][1])):
            if tree[r][c][1][i]:
                ans += 1

print(ans)

