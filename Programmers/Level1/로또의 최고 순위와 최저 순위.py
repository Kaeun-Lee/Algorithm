# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) | https://programmers.co.kr/learn/courses/30/lessons/77484

# Solution_1
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}  # 6개 번호가 모두 일치할 경우 1순위
    answer = []
    min_num = max_num = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_num += 1
        if (lottos[i] in win_nums) or (lottos[i] == 0):
            max_num += 1
    answer.append(rank[max_num])
    answer.append(rank[min_num])
    return answer


# Solution_2
def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]      # index -> 맞힌 개수, 정수 -> 순위
    cnt_0 = lottos.count(0)     # .count(0) -> 0의 개수 계산
    ans = 0
    
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


# Solution_3
def solution(lottos, win_nums):
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]  # set 함수로 중복된 값 제거 후 교집합(&) 연산 수행



test_case1 = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])  # Lottos, win_nums
test_case2 = solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
test_case3 = solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
print(test_case1)  # [3, 5]
print(test_case2)  # [1, 6]
print(test_case3)  # [1, 1]