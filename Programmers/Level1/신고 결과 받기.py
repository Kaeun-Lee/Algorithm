# 2022 KAKAO BLIND RECRUITMENT | https://school.programmers.co.kr/learn/courses/30/lessons/92334#

# Solution_1 -> 2개의 defaultdict 사용. 가장 빠름
from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))  # 중복 신고 제거
    user = defaultdict(set)     # user별 신고한 id 저장
    cnt = defaultdict(int)      # user별 신고당한 횟수 저장

    for r in report:
        a, b = r.split()  # 첫 번째 값은 신고자 id, 두 번째 값은 신고당한 id
        user[a].add(b)    # 신고자가 신고한 id 추가. {'apeach': {'muzi', 'frodo'}, 'frodo': {'neo'}, 'muzi': {'neo', 'frodo'}}  
        cnt[b] += 1       # 신고당한 id의 신고 횟수 추가. {'frodo': 2, 'muzi': 1, 'neo': 2}

    for i in id_list:
        result = 0
        for u in user[i]:  # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


# Solultion_2
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}  # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
  
    for r in set(report):               # {'apeach frodo', 'apeach muzi', 'frodo neo', 'muzi frodo', 'muzi neo'}
        reports[r.split()[1]] += 1      # {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1   

    return answer


# test case
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))  # [2,1,1,0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0,0]