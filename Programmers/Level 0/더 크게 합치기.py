# 코딩 기초 트레이닝


# My Solution
def solution(a, b):
    # return max(int(str(a) + str(b)), int(str(b) + str(a)))
    return int(max(str(a) + str(b), str(b) + str(a)))


# Another Solution
def solution(a, b):
    # return max(int(f"{a}{b}"), int(f"{b}{a}"))
    return int(max(f"{a}{b}", f"{b}{a}"))
