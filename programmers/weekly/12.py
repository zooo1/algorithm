from itertools import permutations

def solution(k, dungeons):
    answer = -1
    filtered_dungeon = []
    for i in range(len(dungeons)):
        min_fatigue_lv = dungeons[i][0]
        if k >= min_fatigue_lv:
            filtered_dungeon.append(dungeons[i])
    permu_list = []
    for i in range(len(filtered_dungeon) + 1):
        permu_list.extend(list(permutations(filtered_dungeon, i)))
    
    for permu in permu_list:
        flag = True
        fatigue_lv = k
        for i in range(len(permu)):
            if fatigue_lv < permu[i][0] or fatigue_lv - permu[i][1] < 0:
                flag = False
                break
            else:
                fatigue_lv -= permu[i][1]
        if flag == True and answer < len(permu):
            answer = len(permu)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))