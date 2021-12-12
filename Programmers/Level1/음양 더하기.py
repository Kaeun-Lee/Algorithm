# 월간 코드 챌린지 시즌2 | https://programmers.co.kr/learn/courses/30/lessons/76501

# Solution_1
def solution(absolutes, signs):
    answer = sum([i*1 if j is True else i*-1 for i, j in zip(absolutes, signs)])  # 'is'로 True인 경우를 분류
    return answer


# Solution_2
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))  # True가 '참' 자체임을 활용



test_case1 = solution([4,7,12], [true,false,true])  # 주어진 true가 boolean True를 의미
test_case2 = solution([1,2,3], [false,false,true]) 
print(test_case1)  # 9
print(test_case2)  # 0