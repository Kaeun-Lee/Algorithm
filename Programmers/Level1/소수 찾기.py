# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12921#

# Solution_1 -> 각 수의 제곱근까지 나머지 판별
def solution(n):
    result = 0
    prime = True
    for i in range(2, n + 1): 
        for a in range(2, int(i  ** 0.5) + 1):
            if i % a == 0:
                prime = False
                break
        if prime == True:
            result += 1
        prime = True
    return result


# Solution_2 -> 에라토스테네스의 체
import math
def solution(n):
    lst = [True] * (n + 1) 
    for i in range(2, int(math.sqrt(n)) + 1):
        if lst[i]:
            j = 2
            while i * j <= n:
                lst[i * j] = False
                j += 1
    return sum(lst[2:])


# Solution_3 -> 에라토스테네스의 체. set 자료형의 차집합 이용
def solution(n):
    num = set(range(2, n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)


# test case
print(solution(10))  # 4
print(solution(5))   # 3