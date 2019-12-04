from itertools import combinations, permutations

def solution(numbers):
    answer = set()
    def is_prime_number(num):
        if num == 2:
            return True
        for n in range(2, num):
            if num%n == 0:
                return False
        return True

    for i in range(1, len(numbers)+1):
        combs = list(map(''.join, combinations(numbers, i)))
        for comb in combs:
            for num in list(map(''.join, permutations(comb, len(comb)))):
                if is_prime_number(int(num)):
                    answer.add(int(num))

    return len(answer)

print(solution("17"))
print(solution("011"))
