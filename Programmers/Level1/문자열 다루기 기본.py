# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12918/solution_groups?language=python3

# Solution_1
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
    return False


# Solution_2
def solution(s):
    return s.isdigit() and len(s) in (4, 6)


# Solution_3 -> try ~ except문, int(). Solution_1, 2보다 오래 걸림
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6


# Solution_4 -> 정규 표현식 이용. 시간 가장 오래 걸림
# ^ : 문자열의 처음, $ : 문자열의 끝
# \d : 숫자를 의미, {4}|{6} : 숫자가 4번 or 6번 반복되는 것을 찾음
# bool을 이용해 결과를 True/False로 return
import re
def solution(s):
    return bool(re.match("^(\d{4}|\d{6})$", s))
   

# test case
print(solution("a234"))  # False
print(solution("1234"))  # True