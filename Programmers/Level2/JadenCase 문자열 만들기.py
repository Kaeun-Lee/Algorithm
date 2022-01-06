# https://programmers.co.kr/learn/courses/30/lessons/12951

# Solution_1
import re
def solution(s):
    answer = []
    s = s.lower()          # 모든 문자를 소문자로 변환 unFollowed -> unfollowed
    s = re.split(" ", s)   # 공백을 기준으로 나눠야 '  unfollowed' -> ' ', 'unfollowed'가 됨
    for i in s:
        i = i.capitalize() # 첫 글자만 대문자로 변경
        answer.append(i)

    return " ".join(answer)



test_case1 = solution("3people unFollowed me")
test_case2 = solution("for the last week")
print(test_case1) # "3people Unfollowed Me"
print(test_case2) # "For The Last Week"