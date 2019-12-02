from collections import deque

def solution(begin, target, words):
    answer = 0xfffff
    flag = 0 

    if target not in words:
        return 0
    
    N = len(begin)
    visited = [0] * len(words)
    Q = deque()
    # Queue 초기화
    i = 0 
    while i < len(words):
        cnt1 = 0
        for j in range(N):
            if begin[j] != words[i][j]:
                cnt1 += 1
        if cnt1 == 1:   
            visited[i] = 1
            Q.append((i, 1))
        i += 1
    
    while Q:
        idx, ans = Q.popleft()
        # print(idx, ans)
        i = 0
        if words[idx] == target:
            return ans
        while i < len(words):
            cnt = 0
            if not visited[i]:

                for j in range(N):
                    if words[idx][j] != words[i][j]:
                        cnt += 1
                if cnt == 1:
                    if words[i] == target:
                        print(words[i], target)
                        flag = 1
                        if answer > ans+1:
                            answer = ans + 1
                
                    visited[i] = 1
                    Q.append((i, ans+1))
            i += 1                    
    return answer if flag else 0

# print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log"]))
print(solution("hot", "lot",["hot", "dot", "dog", "lot", "log"]))

