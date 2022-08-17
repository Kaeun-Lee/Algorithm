# 월간 코드 챌린지 시즌3 | https://school.programmers.co.kr/learn/courses/30/lessons/87389

# Solution_1
def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
      

# test case
print(solution(10))  # 3
print(solution(12))  # 11