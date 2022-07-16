# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12910

# Solution_1
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0 :
        return [-1]
    
    return sorted(answer)


# Solution_2 -> A or B 연산 : A가 True면 A를 반환하고, A가 False면 B를 반환
def solution(arr, divisor):
    return sorted([i for i in arr if i % divisor == 0]) or [-1]


# Solution_3 -> filter 함수 이용, 시간이 좀 더 소요됨
def solution(arr, divisor):
    return sorted(filter(lambda x: x % divisor == 0, arr)) or [-1]


# Solution_4
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]


# test case
print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
print(solution([3, 2, 6], 10))     # [-1]