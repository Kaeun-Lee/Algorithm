# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 양의 정수 x가 하샤드 수 : x의 자릿수 합으로 x가 나누어져야 함

# Solution_1
def solution(x):
    return False if x % sum(map(int, str(x))) else True


# Solution_2
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0

# test case
print(solution(10))  # True
print(solution(12))  # True
print(solution(11))  # False
print(solution(13))  # False