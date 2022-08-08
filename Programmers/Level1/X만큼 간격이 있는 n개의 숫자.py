# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12954

# Solution_1
def solution(x, n):
    answer = [x]
    for _ in range(n - 1):
        answer.append(answer[-1] + x)
    return answer


# Solution_2
def solution(x, n):
    return [i * x for i in range(1, n + 1)]
    

# Solution_3
def solution(x, n):
    return [(i * x) + x for i in range(n)]
    # return [(i + 1) * x for i in range(n)] 과 동일


# test case
print(solution(2, 5))   # [2, 4, 6, 8, 10]
print(solution(4, 3))   # [4, 8, 12]
print(solution(-4, 2))  # [-4, -8]