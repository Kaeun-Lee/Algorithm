# https://programmers.co.kr/learn/courses/30/lessons/77484

# Solution_1
def solution(lottos, win_nums):
    rank ={6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
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
    rank = [6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]


# Solution_3
def solution(lottos, win_nums):
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]