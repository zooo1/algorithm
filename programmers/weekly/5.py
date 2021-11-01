def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    word_order = dict()
    cnt = [0]
    def set_word_order(num, string, cnt):
        for i in range(len(vowels)):
            new_string = string + vowels[i]
            if len(new_string) <= num:
                cnt[0] += 1
                word_order[new_string] = cnt[0]
                # print(new_string, cnt[0])
                set_word_order(num, new_string, cnt)

    for num in range(1, 6):
        set_word_order(num, "", cnt)

    return word_order[word] - 970

print(solution('A'))
print(solution('AA'))
print(solution('AAA'))
print(solution('AAAA'))
print(solution('AAAAA'))
print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))