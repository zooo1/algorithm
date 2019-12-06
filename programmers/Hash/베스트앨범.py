def solution(genres, plays):
    answer = []

    play_list_info = dict()  # 각 장르별로 고유번호, 재생횟수를 저장하는 딕셔너리 (key: value => classic: [[0, 1400], [3, 200]])
    play_list_cnt = dict()  # 각 장르별로 재생횟수를 다 더해놓은 딕셔너리(key:value => 1600: classic) 모든 장르는 재생된 횟수가 다릅니다. 라는 조건을 참고하였음
    
    # 장르별 구분
    for i in range(len(genres)):
        if genres[i] in play_list_info:
            play_list_info[genres[i]].append([plays[i], i])
        else:
            play_list_info[genres[i]] = [[plays[i], i]]

    for genre in play_list_info:
        play_list_info[genre].sort(key=lambda x: x[0], reverse=True)

    play_cnt_info = dict()
    for kind, info in play_list_info.items():
        play_cnt_info[sum(map(lambda x: x[0], info))] = kind
        
    
    while play_cnt_info:
        max_num = max(play_cnt_info.keys())
        genre = play_cnt_info.pop(max_num)
        answer.extend(play_list_info[genre][:2])
        
    answer = [x[1] for x in answer]
    return answer

print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 2500, 500, 500]))
