import sys
input = sys.stdin.readline

N = int(input())
A = [int(x) for x in input().split()]
B, C = map(int, input().split())
ans  = 0
ans += N
for n in range(N):
    A[n] -= B
    if (A[n]>0):
        ans += A[n] // C
        if A[n] % C:
            ans += 1

print(ans)

# 시간 초과 난 코드
import sys
input = sys.stdin.readline

N = int(input())
A = [int(x) for x in input().split()]
B, C = map(int, input().split())
ans = 0
for i in range(len(A)):
    # 총 감독관은 반드시 1명이다.
    ans += 1
    A[i] -= B
    while A[i]>0:
        A[i] -= C
        ans += 1

print(ans)ㄴ