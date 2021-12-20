# 정렬 | https://programmers.co.kr/learn/courses/30/lessons/42747

# Solution_1
from bisect import bisect_left, bisect_right
def solution(citations):
    answer = []
    citations.sort()
    
    for i in range(max(citations), -1, -1): # 6,5,4,...,0
        left_index = bisect_left(citations, i) # 4,3,3,2,2,1,0
        right_index = bisect_right(citations, max(citations)) # 6
        cnt = right_index - left_index # i번 이상 인용된 논문의 수
        if cnt >= i and left_index <= i:
            answer.append(i)
    
    return max(answer)

# Solution_2
from bisect import bisect_left
def solution(citations):
    answer = 0
    result = []
    citations.sort()
    for i in range(citations[-1], -1, -1): # 9,8,7,6,...,0
        h = i
        idx = bisect_left(citations, i)
        if (len(citations) - idx) >= h and idx <= h: # 5-1 >= 1 and 1 <= 1
            result.append(h) # h번, 인덱스
        # i # 인덱스 5개 중 3이면 n-i 이상이 h개 이상, i가 h개 이하
        
    return result[0]


# Solution_3
def solution(citations):
    citations.sort(reverse=True) # [6, 5, 3, 1, 0]
    answer = max(map(min, enumerate(citations, start=1))) # 1) start로 현재 자신보다 큰 수가 몇 개 있는지 판별
    return answer                                         # 2) min(1,6), min(2,5), min(3,3), min(4,1), min(5,0)
                                                          #    해당 인용수 이상의 논문 개수와 해당 논문의 인용수 중 더 작은 숫자를 고름
                                                          # 3) max(1,2,3,1,0) : 이 중 가장 큰 숫자를 뽑아 h-index를 구함


# Solution_4
def solution(citations):
    citations = sorted(citations) # [0, 1, 3, 5, 6]
    l = len(citations) # 5
    for i in range(l): # 0,1,2,3,4
        if citations[i] >= l-i: # 1 >= 5-1, 3 >= 5-2 -> h-index가 큰 경우부터 검사하고 조건에 만족하면 출력
            return l-i
    return 0
        


test_case = solution([3, 0, 6, 1, 5])
print(test_case) # 3