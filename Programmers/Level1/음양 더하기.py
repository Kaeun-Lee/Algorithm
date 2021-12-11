# 월간 코드 챌린지 시즌2 | https://programmers.co.kr/learn/courses/30/lessons/76501

# Solution_1
def solution(absolutes, signs):
    answer = sum([i*1 if j is True else i*-1 for i, j in zip(absolutes, signs)])  # 'is'로 True인 경우를 분류
    return answer