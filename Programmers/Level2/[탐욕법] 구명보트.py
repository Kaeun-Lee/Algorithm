# 탐욕법(Greedy) | https://programmers.co.kr/learn/courses/30/lessons/42885#qna

# Solution_1
def solution(people, limit):
    answer = 0
    people.sort() # 오름차순 정렬
    start = 0
    end = len(people)-1
    
    for _ in range(len(people)): # 가장 작은 수와 가장 큰 수를 더할 것임
        if start != end and start < end: 
            if people[start] + people[end] > limit:    # 한 명만 보트에 타는 경우
                answer += 1
                end -= 1
            elif people[start] + people[end] <= limit: # 두 명이 동시에 보트에 타는 경우
                answer += 1
                start += 1
                end -= 1
        elif start == end: # 보트에 한 명만 남은 경우
            answer += 1
            break
    return answer


# Solution_2 -> while문 이용
def solution(people, limit):
    answer = 0
    people.sort()
    
    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer # 전체 인원 - 짝지은 수 = 보트의 수



test_case1 = solution([70, 50, 80, 50], 100)
test_case2 = solution([70, 80, 50], 100)
print(test_case1) # 3
print(test_case2) # 3