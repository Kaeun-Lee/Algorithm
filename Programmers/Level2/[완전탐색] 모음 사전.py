# 완전탐색 | https://school.programmers.co.kr/learn/courses/30/lessons/84512

# Solution_1
from itertools import product
def solution(word):
    char = ['A', 'E', 'I', 'O', 'U']
    dic = []
    for i in range(1, 6):
        tmp = list(map(lambda x: list(x), product(char, repeat = i)))
        for j in range(len(tmp)):
            dic.append(''.join(tmp[j]))
    dic = sorted(dic)
    return dic.index(word) + 1


# Solution_2 -> list comprehension, extend 함수로 반복문 줄임
from itertools import product
def solution(word):
    a = ["A", "E", "I", "O", "U"]
    total = []
    for i in range(1, 6):
        c = [''.join(j) for j in product(a, repeat=i)]
        total.extend(c)
    total.sort()
    return total.index(word) + 1


# Solution_3 -> product안에 문자열 'AEIOU'를 넣어도 됨, ('A', 'A')도 join이 가능
from itertools import product
def solution(word):
    return sorted([''.join(c) for i in range(5) for c in product("AEIOU", repeat=i + 1)]).index(word) + 1


# test case
print(solution("AAAAE"))  # 6
print(solution("AAAE"))   # 10
print(solution("I"))      # 1563
print(solution("EIO"))    # 1189