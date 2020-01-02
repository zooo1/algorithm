N = list(map(int, input().replace('',' ').split()))
cnt_ary = [0] * 10
answer = 0
for num in N:
    if num == 6 or num == 9:
        min_idx = 6 if cnt_ary[6] < cnt_ary[9] else 9
        if cnt_ary[min_idx] >= max(cnt_ary):
            answer += 1
        cnt_ary[min_idx] += 1

    else:
        if cnt_ary[num] >= max(cnt_ary):
            answer += 1
        cnt_ary[num] += 1
        
print(answer)