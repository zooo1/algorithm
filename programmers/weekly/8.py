def solution(sizes):
    zipped = list(zip(*sizes))
    max_a = max(zipped[0])
    max_b = max(zipped[1])
    if max_a >= max_b:
        for idx in range(len(zipped[1])):
            if sizes[idx][0] < sizes[idx][1]:
                sizes[idx] = [sizes[idx][1], sizes[idx][0]]
    else:
        for idx in range(len(zipped[0])):
            if sizes[idx][1] < sizes[idx][0]:
                sizes[idx] = [sizes[idx][1], sizes[idx][0]]

    re_zipped = list(zip(*sizes))
    re_max_a = max(re_zipped[0] )
    re_max_b = max(re_zipped[1] )
    return re_max_a * re_max_b


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))