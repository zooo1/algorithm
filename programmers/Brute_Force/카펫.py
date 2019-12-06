def solution(brown, red):
    factor = []
    N = brown+red

    # 숫자가 큰 순서대로(가로가 세로보다 길거나 같음) 약수를 저장해두는 factor 배열을 생성한다.
    for num in range(N, 0, -1):
        if N%num == 0:
            factor.append(num)
    i, j = 0, len(factor)-1

    # 갈색, 빨간색의 카펫 갯수와 동일한 약수를 찾으면 리턴
    while i <= j:
        r, c = factor[i], factor[j]
        if 2*(r+c) - 4 ==  brown and (r-2)*(c-2)==red:
            return [r, c]
        i += 1
        j -= 1

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
print(solution(20, 12))

