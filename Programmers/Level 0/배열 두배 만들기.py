# 코딩테스트 입문


# My Solution
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))


# Another Solution -> list comprehension 사용
def solution(numbers):
    return [i * 2 for i in numbers]
