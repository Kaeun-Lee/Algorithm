# 2019 KAKAO BLIND RECRUITMENT | https://school.programmers.co.kr/learn/courses/30/lessons/42889

# count()는 O(N)의 시간 복잡도 소요
# Solution_1
from collections import Counter
def solution(N, stages):
    lst = [0] * (N + 1)
    stage_cnt = Counter(stages).most_common(len(stages))  # list를 return. [(2, 3), (3, 2), (1, 1), (6, 1), (4, 1)]
    stage_cnt = sorted(stage_cnt, key=lambda x: x[0])     # [(1, 1), (2, 3), (3, 2), (4, 1), (6, 1)]
    user = len(stages)
    for s, n in stage_cnt:
        lst[s - 1] = (s, n / user)
        user -= n
    for i in range(len(lst)):  # 스테이지에 도달한 유저가 없는 경우
        if lst[i] == 0:
            lst[i] = (i + 1, 0)
    result = sorted(lst[:-1], key=lambda x: (x[1], -x[0]), reverse=True)  # 실패율 내림차순 후, 실패율이 같은 경우 번호 오름차순
    return [i[0] for i in result]


# Solution_2 -> Counter의 key와 value 이용
# Counter는 dictionary와 달리 key가 없어도 0을 return함
from collections import Counter
def solution(N, stages):
    stats = Counter(stages)
    total = len(stages)
    result = []
    for i in range(1, N + 1):
        failure = stats[i] / total if total > 0 else 0  # 분모가 0이 되는 경우 고려
        result.append((i, failure))
        total -= stats[i]
    result = sorted(result, key=lambda x: (x[1], -x[0]), reverse=True)
    return [r[0] for r in result]


# Solution_3 -> dictionary 이용, 속도 가장 빠름. 분모가 0일 때 % 아닐 때
from collections import Counter
def solution(N, stages):
    stats = Counter(stages)
    result = {}  # {1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}
    denominator = len(stages)
    for stage in range(1, N + 1):
        if denominator != 0:
            result[stage] = stats[stage] / denominator
            denominator -= stats[stage]
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)  # result[x]: value를 기준으로 정렬된 key를 return


# Solution_4
def solution(N, stages):
    fail = []
    info = [0] * (N + 2)  # [0, 0, 0, 0, 0, 0, 0]
    for stage in stages:
        info[stage] += 1  # [0, 1, 3, 2, 1, 0, 1]
    for i in range(N):  # 0, 1, 2, 3, 4
        be = sum(info[(i + 1):])  # 8, 7, 4, 2, 1
        yet = info[i + 1]         # 1, 3, 2, 1, 0
        if be == 0:
            fail.append((i + 1, 0))
        else:
            fail.append((i + 1, yet / be))
    return [item[0] for item in sorted(fail, key=lambda x: x[1], reverse=True)]


# test case
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))               # [4,1,2,3]