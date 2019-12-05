def solution(participant, completion):
    check_participant = dict()
    for person in participant:
        if person in check_participant:
            check_participant[person] += 1
        else:
            check_participant[person] = 1

    for person in completion:
        check_participant[person] -= 1

    for person in check_participant:
        if check_participant[person]:
            return person

print(solution(["leo", "kiki", "eden"], ["kiki", "eden"]))