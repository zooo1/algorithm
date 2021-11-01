def solution(table, languages, preference):
    score_info = {}
    scores = {}
    answers = []
    for row in range(len(table)):
        info = table[row].split(' ')
        content = info[0]
        langs = info[1:][::-1]
        score_info[content] = {}
        for idx in range(len(langs)):
            lang = langs[idx]
            if lang in languages:
                score_info[content][lang] = idx+1
    
    for key in score_info.keys():
        scores[key] = 0
        for k, v in score_info[key].items():
            idx = languages.index(k)
            scores[key] += preference[idx] * v

    max_value = max(list(scores.values()))
    for k, v in scores.items():
        if v >= max_value:
            max_value = v
            answers.append(k)
    answers.sort()
    return answers[0]

print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"]	, [7, 5, 5]	))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"],	[7, 5])	)