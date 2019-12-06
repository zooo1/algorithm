def solution(genres, plays):
    answer = []
    play_list_info = dict()
    play_list_cnt = dict()
    for i in range(len(genres)):
        if genres[i] in play_list_info:
            play_list_info[genres[i]].append([plays[i], i])
        else:
            play_list_info[genres[i]] = [[plays[i], i]]

    play_list_info = {kind:sorted(play_cnt, reverse=True) for (kind, play_cnt) in play_list_info.items()}

    play_cnt_info = dict()
    for kind, info in play_list_info.items():
        play_cnt_info[sum(map(lambda x: x[0], info))] = kind

    while play_cnt_info:
        max_num = max(play_cnt_info.keys())
        kind = play_cnt_info.pop(max_num)
        print(kind)
        cnt, idx = 0, 0
        if len(play_list_info[kind]) == 1:
            answer.append(play_list_info[kind][0])
        else:
            while cnt < 2:
                while idx < len(play_list_info[kind]):
                    value = play_list_info[kind][idx][0]
                    j = idx+1
                    if j < len(play_list_info[kind]) and value == play_list_info[kind][j][0]:
                        while idx < len(play_list_info[kind]) and play_list_info[kind][idx][0] == value:
                            idx += 1
                        answer.append(play_list_info[kind][idx-1])
                        answer.append(play_list_info[kind][idx-2])

                        cnt += 2
                        if cnt == 2:
                            break

                    else:
                        answer.append(play_list_info[kind][idx])
                        idx += 1
                        cnt += 1
                        if cnt == 2:
                            break

    answer = [x[1] for x in answer]


    return answer
