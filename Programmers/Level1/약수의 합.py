# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12928

# Solution_1
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer


# Solution_2 -> 쌍이 되는 약수를 한 번에 고려. 시간이 훨씬 줄어듦
def solution(n):
    result = 1 + n  # (1, n)쌍은 자명하니 처음부터 더해줌
    for i in range(2, int(n ** 0.5) + 1):  # 약수 후보 : 2 ~ sqrt(n)
        if n % i == 0:            # 만약 divider가 약수면
            result += i           # result에 더해줌
            i_pair = n // i       # 쌍이 되는 다른 약수
            if i_pair != i:       # 쌍이 되는 약수가 i와 다를 경우. ex) 16 = 4*4면, 4를 1번만 더해야 함
                result += i_pair  # 쌍이 되는 약수를 더해줌
    return result


# Solution_3 -> (n // 2)까지 확인, []를 제외하면 시간이 더 줄어듦
# n이 아닌 약수 중 가장 큰 수는 (n // 2)이기 때문에, 처음에 n을 더해주고 그 다음에는 (n // 2)까지만 확인하면 됨
def solution(n):
    return n + sum(i for i in range(1, (n // 2) + 1) if n % i == 0)  # n은 1과 n으로 나누어떨어지니 미리 더해줌


# Solution_4 -> list comprehension 이용, []를 제외하면 시간이 더 늘어남
def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])


# Solution_5 -> filter 이용
def solution(n):
    return sum(filter(lambda x: n % x == 0, range(1, n + 1)))


# test case
print(solution(12))  # 28
print(solution(5))   # 6
print(solution(9))   # 13