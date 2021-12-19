# 정렬 | https://programmers.co.kr/learn/courses/30/lessons/42747

# Solution_1
from bisect import bisect_left, bisect_right
def solution(citations):
    answer = []
    citations.sort()
    
    for i in range(max(citations), -1, -1): # 6, 5, 4, ..., 0
        left_index = bisect_left(citations, i) # 4, 3, 3, 2, 2, 1, 0
        right_index = bisect_right(citations, max(citations)) # 6
        cnt = right_index - left_index # i번 이상 인용된 논문의 수
        if cnt >= i and left_index <= i:
            answer.append(i)
    
    return max(answer)

# Solution_2

test_case = solution([3, 0, 6, 1, 5])
print(test_case) # 3