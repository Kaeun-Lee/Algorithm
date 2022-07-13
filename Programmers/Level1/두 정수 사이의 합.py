# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12912

# Solution_1
def solution(a, b):  
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

    # if a == b:
    #     return a
    # elif a > b:
    #     a, b = b, a
    # return sum(range(a, b + 1))


# Solution_2
def solution(a, b):
    return a if a == b else sum(range(a, b + 1)) if a < b else sum(range(b, a + 1))


# Solution_3 -> min, max 이용
def solution(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# Solution_4 -> 수학 공식 (n x (n + 1) / 2) 변형 이용, 시간 복잡도 : O(1)
# n -> (abs(a - b) + 1) : a ~ b 사이의 정수 개수
# (n + 1) / 2 -> (a + b) / 2 : 처음과 끝 2개 정수씩 쌍을 이뤘을 때 모두 합이 같다는 걸 이용해서 다 더한 뒤 2로 나누기
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2


# test case
print(solution(3, 5))  # 12
print(solution(3, 3))  # 3
print(solution(5, 3))  # 12