# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾸기

# Solution_1
def solution(s):
    idx = 0
    result = ''
    for i in s:
        if i != ' ':
            if idx % 2 == 0:
                result += i.upper()
            else:
                result += i.lower()
            idx += 1  # 공백이 아닐 경우 idx 증가
        else:
            result += i
            idx = 0  # 공백일 경우 idx 초기화
    return result


# Solution_2 -> map, lambda 이용
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))


# Solution_3 -> list comprehension
def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(" ")])


# Solution_4
def solution(s):
    words = s.split(' ')  # ['try', 'hello', 'world']
    for i, word in enumerate(words):  # 0 try
        word = list(word)  # ['t', 'r', 'y']
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                word[idx] = char.upper()
            else:
                word[idx] = char.lower()
        words[i] = ''.join(word)  # TrY
    return ' '.join(words)


# test case
print(solution("try hello world"))  # "TrY HeLlO WoRlD"