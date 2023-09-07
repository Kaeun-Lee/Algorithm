# 코딩 기초 트레이닝


# My Solution
def solution(names):
    return [names[i * 5] for i in range((len(names) - 1) // 5 + 1)]


# Another Solution 1 -> 가장 빠름
def solution(names):
    return names[::5]


# Another Solution 2
def solution(names):
    return [names[i] for i in range(0, len(names), 5)]


# Another Solution 3
def solution(names):
    return [names[i] for i in range(len(names)) if i % 5 == 0]
