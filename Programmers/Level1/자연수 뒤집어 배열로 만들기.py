# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12932

# Solution_1
def solution(n):
    n = str(n)  # n = '12345'
    return [int(n[i]) for i in range(len(n) - 1, -1, -1)]


# Solution_2 -> reversed(주어진 문자열의 반전된 반복자 제공) 이용
def solution(n):
    return list(map(int, reversed(str(n)))) 


# Solution_3 -> list 슬라이싱 활용
def solution(n):
    return [int(i) for i in str(n)][::-1]


# test case
print(solution(12345))  # [5, 4, 3, 2, 1]