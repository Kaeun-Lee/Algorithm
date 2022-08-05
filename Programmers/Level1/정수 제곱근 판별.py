# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12934

# Solution_1 -> 문자열로 변환해 첫 번째 소숫점이 '0'인지 확인
from math import sqrt
def solution(n):
    return (sqrt(n) + 1) ** 2 if f'{sqrt(n)}'[-1] == '0' else -1


# Solution_2 -> '% 1' 연산으로 실수, 정수 판별
def solution(n):
    x = n ** 0.5
    return -1 if x % 1 else (x + 1) ** 2
    # return -1 if sqrt(n) % 1 else (sqrt(n) + 1) ** 2 
    # return (x + 1) ** 2  if int(x) == x else -1


# Solution_3 -> float 객체에 사용할 수 있는 is_integer()
def solution(n):
    x = n ** 0.5
    return -1 if not x.is_integer() else (x + 1) ** 2  # float.is_integer(x)와 동일
   

# Solution_4 -> pow 함수 사용
def solution(n):
    x = pow(n, 0.5)
    return pow(x + 1, 2) if int(x) == x else -1


# test case
print(solution(121))  # 144
print(solution(3))    # -1