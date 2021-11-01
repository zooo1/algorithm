import re

def solution(weights, head2head):
    answer = []

    scores = [int(0 if len(list(filter(lambda x: x == 'L' or x == 'W',list(head2head[i]))) is 0 else round(float(len(re.findall(r'W', head2head[i]))) /(len(list(filter(lambda x: x == 'L' or x == 'W',list(head2head[i])))) - 1) , 6) * 100000) + weights[i] for i in range(len(head2head))]
    for boxer_idx in range(len(weights)):

        indices = [i for i, x in enumerate(head2head[boxer_idx]) if x == 'W']
        for idx in indices:
            if weights[boxer_idx] < weights[idx]:
                scores[boxer_idx] += 1000

    for _ in range(len(weights)):
        max_score = max(scores)
        max_score_idx = scores.index(max_score)
        scores[max_score_idx] = 0
        answer.append(max_score_idx + 1)
    return answer


print(solution([50,82,75,120],	["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86],	["NLW","WNL","LWN"]))
print(solution([60,70,60],	["NNN","NNN","NNN"]))