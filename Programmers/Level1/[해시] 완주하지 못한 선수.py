# 해시 | https://programmers.co.kr/learn/courses/30/lessons/42576

# Solution_1   
def solution(participant, completion):
    person = {}
    
    # 참가자 확인
    for i in participant:
        if i not in person:
            person[i] = 1   # 명단에 없으면 이름과 1을 넣어줌
        else:
            person[i] += 1  # 명단에 있으면 해당 이름의 value값 +1 -> 동명이인이 있음을 고려
            
    # 완주한 선수 확인
    for j in completion:
        if j in person:
            person[j] -= 1   # 완주한 선수는 해당 이름의 value값 -1
            
    # 완주하지 못한 선수 확인
    for k, v in person.items():
        if v >= 1:
            return k


# Solution_2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)  # Counter 객체를 이용하면 뺄셈이 가능 / 일반 dict는 뺄셈 불가능
    return list(answer.keys())[0]  # answer.keys() -> dict_keys(['leo'])


# Solution_3
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part  # dic에 hash 값을 key로, 사람 이름을 value로 넣음
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    
    return answer
            
            
# Solution_4
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]: # 참가자와 완주자가 매칭되지 않으면 return
            return participant[i]
    return participant[-1]  # 동명이인이 있는 경우 정렬된 participant의 마지막 사람을 return


# Solution_5 -> Solution_4와 비슷
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]



test_case1 = solution(["leo", "kiki", "eden"], ["eden", "kiki"])
test_case2 = solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
test_case3 = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print(test_case1)  # leo
print(test_case2)  # vinko
print(test_case3)  # mislav