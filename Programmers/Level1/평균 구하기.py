# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12944

# Solution_1
def solution(arr):
    return sum(arr) / len(arr)


# Solution_2 -> reduce 이용, 시간 효율 떨어짐
from functools import reduce

def solution(arr):
    return reduce(lambda x, y: x + y, arr) / len(arr)


# Solution_3 -> 통계모듈 이용, 시간 효율 매우 떨어짐
import statistics

def solution(arr):
    return statistics.mean(arr)


# test case
print(solution([1, 2, 3, 4]))  # 2.5
print(solution([5, 5]))        # 5