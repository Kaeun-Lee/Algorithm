# 탐욕법(Greedy) | https://school.programmers.co.kr/learn/courses/30/lessons/42883

# Solution_1 -> (성공) stack 사용
def solution(number, k):
    stack = []
    for i in map(int, number):
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k != 0:
        stack = stack[:-k]
    return ''.join(map(str, stack))


# Solution_2 -> (실패) combiantions 사용
from itertools import combinations
def solution(number, k):
    return str(max(int(''.join(i)) for i in combinations(number, len(number)-k)))


# Solution_3 -> Solution_1과 유사한 풀이
def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:len(number)-k])

    
# test case
print(solution("1924", 2))        # "94"
print(solution("1231234", 3))     # "3234"
print(solution("4177252841", 4))  # "775841"