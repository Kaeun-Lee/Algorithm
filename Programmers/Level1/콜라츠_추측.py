# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12943

# Solution_1 
def solution(num):
    if num == 1:
        return 0
    
    answer = 0
    while num > 1:
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        answer += 1
        if answer == 500 and num != 1:
            return -1
        elif num == 1:
            return answer


# Solution_2 -> 다른 while문 풀이, Solution_1보다 조금 빠름
def solution(num):
    cnt = 0
    while cnt < 501:  # cnt == 500이면서 num == 1인 경우를 포함
        if num == 1:
            return cnt
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        cnt += 1
    return -1


# Solution_3 -> for문 이용
def solution(num):
    for i in range(1, 501):
        if num == 1:
            return i - 1
        
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            return i
    return -1


# test case
print(solution(6))       # 8
print(solution(16))      # 4
print(solution(626331))  # -1