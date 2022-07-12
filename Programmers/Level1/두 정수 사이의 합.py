# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12912

# Solution_1
def solution(a, b):  
    if a > b:
        a, b = b, a
    return sum(list(range(a, b+1)))

# Solution_2
def solution(a, b):
    return a if a == b else sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))


print(solution(3, 5))  # 17