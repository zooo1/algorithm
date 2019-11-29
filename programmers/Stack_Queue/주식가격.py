from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        cnt = 0
        for i in range(len(prices)):
            if price > prices[i]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))