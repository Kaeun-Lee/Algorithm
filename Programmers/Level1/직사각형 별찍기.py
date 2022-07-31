# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12969/solution_groups?language=python3

# Solution_1
from turtle import hideturtle


n, m = map(int, input().split())
answer = ''
for i in range(m):
    for j in range(n):
        answer += '*'
    answer += '\n'
print(answer)   


# Solution_2
n, m = map(int, input().strip().split(' '))
print(('*' * n + '\n') * m)


# Solution_3
n, m = map(int, input().split(' '))
for _ in range(m):
    print('*' * n)


# Solution_4
n, m = map(int, input().split(' '))
for i in range(m):
    for j in range(n):
        print('*', end='')
    print('')  # 또는 print()


# test case
# input : 5 3
# < output >
# *****
# *****
# *****