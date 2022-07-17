# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12903

# Solution_1
def solution(s):
    idx = len(s) // 2 
    return s[idx - 1 : idx + 1] if len(s) % 2 == 0 else s[idx]


# Solution_2 -> if문 사용 X
def solution(s):
    return s[(len(s) - 1) // 2 : len(s) // 2 + 1]


# Solution_3 -> 끝 범위를 - 값으로 표현
def solution(s):
    a = len(s)
    if a % 2  == 0:
        a = (a - 2) // 2
    else:
        a = (a - 1) // 2
    return s[a:-a]


# test case
print(solution("abced"))  # "c"
print(solution("qwer"))   # "we"