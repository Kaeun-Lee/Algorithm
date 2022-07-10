# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12919/solution_groups?language=python3

# Solution_1 -> index 함수 활용
def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"


# test case
print(solution(["Jane", "Kim"]))  # "김서방은 1에 있다"