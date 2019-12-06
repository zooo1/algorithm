from itertools import permutations
def solution(numbers):
    answer = '0'
    perms = permutations(numbers, len(numbers))
    for perm in perms:
        ans = ''
        for p in perm:
            ans += str(p)
        if int(ans) > int(answer):
            answer = ans
    return answer

print(solution([3, 30, 34, 5, 9]))