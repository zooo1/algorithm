from itertools import combinations

def solution(clothes):
    answer = 1
    clothes_info = dict()
    for name, kind in clothes:
        if kind in clothes_info:
            clothes_info[kind] += 1
        else:
            clothes_info[kind] = 1

    for cnt in clothes_info.values():
        answer *= (cnt+1)

    return answer -1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["jean","pants"], ["slacks", "pants"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))