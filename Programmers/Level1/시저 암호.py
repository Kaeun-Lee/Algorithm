# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12926/solution_groups?language=python3

# Solution_1
def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # z : 25, Z : 51
    s = list(s)
    for i in range(len(s)):
        idx = alpha.find(s[i])
        if idx != -1:
            if idx == 25 or idx + n > 25:
                idx = idx - 26
            if s[i].islower():
                 s[i] = alpha[idx + n]
            else:
                s[i] = alpha[idx + n].upper()
    return ''.join(s)


# Solution_2 -> ord와 나머지 사용 
# ord('A') = 65, ord('Z') = 90, ord('a') = 97, ord('z') = 122
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return ''.join(s)


# Solution_3 -> 가장 빠름
def solution(s, n):
    lower_list = 'abcdefghijklmnopqrstuvwxyz'
    upper_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = []
    for i in s:
        if i == " ":
            result.append(" ")
        elif i.islower():
            new = lower_list.find(i) + n
            result.append(lower_list[new % 26])
        else:
            new = upper_list.find(i) + n
            result.append(upper_list[new % 26])
    return "".join(result)  


# Solution_4
def solution(s, n):
    answer = ''
    for i in s:
        if i:
            if 'A' <= i <= 'Z':
                answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            elif 'a' <= i <= 'z':
                answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            else:
                answer += ' '
    return ''.join(answer)


# test case
print(solution("AB", 1))     # "BC"
print(solution("z", 1))      # "a"
print(solution("a B z", 4))  # "e F d"