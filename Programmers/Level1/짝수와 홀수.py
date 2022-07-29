# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12937

# Solution_1
def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'


# Solution_2
def solution(num):
    return "Odd" if num % 2 else "Even"


# Solution_3 -> & 연산자로 비트 연산을 한 숫자를 list의 idx로 사용
def solution(num):
    return ["Even", "Odd"][num & 1]  # 011 & 001 = 1. 2진 비트는 1번째 비트 자리에 의해 홀짝이 결정됨


# Solution_4 -> 논리 연산자 활용. 'Odd'와 'Even'은 True임
# (1 and 'Odd') or Even
# -> A and B에서 A가 1이면 B값을 따르고, A가 0이면 B는 보지않고 and 연산이 0으로 종료되어 0 or Even 연산으로 넘어감
def solution(num):
    return (num % 2 and 'Odd') or 'Even'  # (0(False) and True) or True / (1(True) and True) or True


# test case
print(solution(3))  # "Odd"
print(solution(4))  # "Even"