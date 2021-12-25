# 2020 KAKAO BLIND RECRUITMENT | https://programmers.co.kr/learn/courses/30/lessons/60057

# Solution_1
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