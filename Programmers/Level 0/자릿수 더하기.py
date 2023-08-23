# 코딩테스트 입문


# My Solution
def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n //= 10
    return answer


# My Solution Refactoring -> divmod 사용
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer


# Another Solution 1 -> 문자화 한 뒤 sum 수행
def solution(n):
    return sum(map(int, str(n)))


# Another Solution 2
def solution(n):
    return sum(int(i) for i in str(n))
