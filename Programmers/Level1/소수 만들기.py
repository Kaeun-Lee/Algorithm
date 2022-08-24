# Summer/Winter Coding(~2018) | https://school.programmers.co.kr/learn/courses/30/lessons/12977

# Solution_1
from itertools import combinations
def solution(nums):
    cnt = 0
    a = list(combinations(nums, 3))  # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    for i in map(lambda x: sum(x), a):  # 6, 7, 8, 9
        ch = True
        for j in range(2, int(i ** 0.5) + 1): # 2
            if i % j == 0:
                ch = False
                break
        if ch == True:
            cnt += 1
    return cnt


# Solution_2 -> for ~ else 구문 이용
# for ~ else : for문이 중간에 break 등으로 끊기지 않고 끝까지 수행되었을 때 실행됨
from itertools import combinations
def solution(nums):
    answer = 0
    for a in combinations(nums, 3):
        cand = sum(a)
        for j in range(2, int(cand ** 0.5) + 1):
            if cand % j == 0:
                break
        else:
            answer += 1  
    return answer  


# test case
print(solution([1, 2, 3, 4]))     # 1
print(solution([1, 2, 7, 6, 4]))  # 4