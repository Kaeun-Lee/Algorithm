# 코딩 기초 트레이닝


# My Solution
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0


# Another Solution -> boolean 활용
def solution(number, n, m):
    # return int((number % n == 0) & (number % m == 0))
    return int(number % n == 0 and number % m == 0)
