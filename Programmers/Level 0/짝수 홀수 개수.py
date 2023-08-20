# 코딩테스트 입문


# My Solution
def solution(num_list):
    even_cnt = sum(i % 2 == 0 for i in num_list)
    return [even_cnt, len(num_list) - even_cnt]


# Another Solution -> indexing 활용
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        answer[i % 2] += 1
    return answer
