# 월간 코드 챌린지 시즌1 | https://programmers.co.kr/learn/courses/30/lessons/70128

# Solution_1
def solution(a, b):
    answer = sum([x*y for x, y in zip(a, b)])
    return answer


# Solution_2
solution = lambda a, b : sum(x*y for x,y in zip(a,b))



test_case1 = solution([1,2,3,4], [-3,-1,0,2])
test_case2 = solution([-1,0,1], [1,0,-1])
print(test_case1)  # 3
print(test_case2)  # -2