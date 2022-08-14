# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12917

# Solution_1 -> 가장 느림
def solution(s):
    return ''.join(sorted(sorted(s, key=str.upper), key=str, reverse=True))


# Solution_2 -> 가장 빠름
def solution(s):
    return ''.join(sorted(s, reverse=True))


# Solution_3
def solution(s):
    lower = []
    upper = []
    for i in s:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    lower.sort(reverse=True)
    upper.sort(reverse=True)
    return ''.join(lower) + ''.join(upper)


# test case
print(solution("Zbcdefg"))  # gfedcbZ