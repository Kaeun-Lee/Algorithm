# 2020 KAKAO BLIND RECRUITMENT | https://programmers.co.kr/learn/courses/30/lessons/60057

# Solution_1
def solution(s):
    results = []

    for i in range(1, (len(s) // 2)+1):
        cnt = 0
        answer = ""

        for j in range(0, len(s), i):
            if s[j:j+i] != s[j+i:j+i+i] :
                if cnt > 0:
                    answer += str(cnt + 1) + s[j:j+i]
                    cnt = 0
                else:
                    answer += s[j:j+i]
            else:
                cnt += 1

        results.append(answer)

    minimum = len(s)
    for el in results:
        if len(el) < minimum and len(el) != 0:
            minimum = len(el)

    return minimum


# Solution_2
def solution(s):
    start = ''
    cnt = 1
    answer = ''
    
    for i in range(len(s)):
        start += s[0:i+1]
        for j in range(0, len(s), len(start)):
            next = s[len(start)+j : len(start)+j+len(start)]
            if next == start:
                cnt += 1
            elif next != start:
                answer += str(cnt)
                answer += start
                cnt = 1
                       
    return answer



test_case1 = solution("aabbaccc")
test_case2 = solution("ababcdcdababcdcd")
test_case3 = solution("abcabcdede")
test_case4 = solution("abcabcabcabcdededededede")
test_case5 = solution("xababcdcdababcdcd")
print(test_case1) # 7
print(test_case2) # 9
print(test_case3) # 8
print(test_case4) # 14
print(test_case5) # 17
