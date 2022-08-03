# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12915

# Solution_1 ->  lambda의 기준 우선순위 이용
# sorted(iter, key=lambda x: (기준1, 기준2))
# sorted(iter, key=lambda x: (x[0], -x[1]), reverse=True) 0번째 원소로 내림차순 정렬 후, 1번째 원소로 오름차순 정렬
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x)) # n번째 문자를 기준으로 정렬 후, x 문자를 기준으로 정렬


# Solution_2 -> 먼저 1번 정렬하고 그 다음 n번째 문자를 기준으로 정렬
def solution(strings, n):
    strings.sort()  
    return sorted(strings, key=lambda x: x[n])


# Solution_3
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])


# Solution_4 -> operator.itemgetter() 이용
from operator import itemgetter
def solution(strings, n):
    return sorted(sorted(strings), key=itemgetter(n))


# test case
print(solution(["sun", "bed", "car"], 1))    # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]