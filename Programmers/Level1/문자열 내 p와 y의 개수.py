# 연습 문제 | https://programmers.co.kr/learn/courses/30/lessons/12916

# Solution_1
def solution(s):
    s = s.lower() 
    answer = 0
    
    for i in s:
        if i == 'p':
            answer += 1
        elif i == 'y':
            answer -= 1
            
    if answer != 0:
        return False
    return True


# Solution_2 -> count() 집계 함수 이용
# *count 함수 : 문자열 내부에서 특정 문자나 문자열의 개수를 카운트
def solution(s):
    return s.lower().count('p') == s.lower().count('y')


# Solution_3
from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return c['p'] == c['y']


# test case
print(solution("pPoooyY"))  # True
print(solution("Pyy"))      # False