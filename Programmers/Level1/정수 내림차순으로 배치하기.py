# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12933

# Solution_1
def solution(n):
    answer = 0
    temp = sorted(map(int, str(n)))
    
    for i, n in enumerate(temp):
        answer += (10 ** i) * n
    return answer


# Solution_2 
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))  # sorted는 list를 return


# test case
print(solution(118372))  # 873211