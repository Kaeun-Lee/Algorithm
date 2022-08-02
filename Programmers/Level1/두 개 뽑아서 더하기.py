# 월간 코드 챌린지 시즌 1 | https://school.programmers.co.kr/learn/courses/30/lessons/68644

# Soluion_1 -> set으로 중복 제거
def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1): 
        for j in range(i + 1, len(numbers)): 
            answer.append(numbers[i] + numbers[j])
    return sorted(set(answer))  # sorted()는 list를 return


# Solution_2 -> 조합 이용. Solution_1보다 시간 좀 더 걸림
from itertools import combinations
def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))  # [(5, 0), (5, 2), (5, 7), (0, 2), (0, 7), (2, 7)]

    for i in l:
        answer.append(i[0] + i[1])
    return sorted(set(answer))
    # return sorted(set(sum(i) for i in list(combinations(numbers, 2))))
    # return sorted(set(map(sum, combinations(numbers, 2))))


# test case
print(solution([2, 1, 3, 4, 1]))  # [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7]))     # [2, 5, 7, 9, 12]