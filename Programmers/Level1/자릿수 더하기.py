# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12931

# Solution_1 -> 몫을 더함
def solution(n):
    answer = 0
    for i in range(len(str(n)) - 1, -1, -1):
        answer += n // (10 ** i)
        n = n % (10 ** i)
    return answer


# Solution_2 -> 재귀 함수 이용. 나머지를 더함
def solution(n):
    if n < 10:
        return n
    return (n % 10) + solution(n // 10)


# Solution_3 -> Solution_1보다 시간이 좀 더 걸림
def solution(n):
    return sum(map(int, str(n)))  # map(f, iterable)


# test case
print(solution(123))  # 6
print(solution(987))  # 24