# 코딩테스트 입문


# My Solution
def solution(array):
    array.sort()
    return array[len(array) // 2]


# Another Solution -> sorted 사용. sort보다 느림
def solution(array):
    return sorted(array)[len(array) // 2]
