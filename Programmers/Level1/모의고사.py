# 완전탐색 | https://school.programmers.co.kr/learn/courses/30/lessons/42840

# Solution_1
# % 연산 : 어떤 수를 x로 나눈면 결과는 무조건 x보다 작음. 특정 범위 내 숫자를 구할 때 자주 사용
def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = [[1, 0], [2, 0], [3, 0]]
    
    for i in range(len(answers)):  # 0,1 2 3 4
        if answers[i] == s1[i % len(s1)]:
            answer[0][1] += 1
    for i in range(len(answers)):
        if answers[i] == s2[i % len(s2)]:
            answer[1][1] += 1
    for i in range(len(answers)):
        if answers[i] == s3[i % len(s3)]:
            answer[2][1] += 1
    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    max_ = 0
    for i in answer:
        if i[1] > max_:
            max_ = i[1]
    
    result = []
    for i in answer:
        if i[1] == max_:
            result.append(i[0])
    return result


# Solution_2 -> enumerate 이용
def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):  # 0 1, 1 2, 2 3, 3 4, 4 5
        if answer == s1[idx % len(s1)]:
            score[0] += 1
        if answer == s2[idx % len(s2)]:
            score[1] += 1
        if answer == s3[idx % len(s3)]:
            score[2] += 1

    for idx, s in enumerate(score):  # 0 5, 1 0, 1 0
        if s == max(score):
            result.append(idx + 1)
    return result


# Solution_3
def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):  # 0 1, 1 2, 2 3, 3 4, 4 5
        for i, v in enumerate(p):    # 0 [1, 2, 3, 4, 5]
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


# Solution_4 -> cycle, next 사용 
# cycle generator로 처리하여 공간복잡도 줄임
from itertools import cycle
def solution(answers):
    students = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(students[i]) == num:
                scores[i] += 1
    highest = max(scores)
    return [i + 1 for i, v in enumerate(scores) if v == highest]


# test case
print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]