# 코딩테스트 입문


# My Solution -> set의 교집합 사용
def solution(s1, s2):
    return len(set(s1) & set(s2))


# Another Solution -> dictionary의 get 함수 사용
def solution(s1, s2):
    dic = {i: 1 for i in s1}
    return sum(dic.get(j, 0) for j in s2)
