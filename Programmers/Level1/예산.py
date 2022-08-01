# Summer/Winter Coding(~2018) | https://school.programmers.co.kr/learn/courses/30/lessons/12982

# Solution_1 -> budget에서 d의 가장 작은 값을 빼면서 cnt의 최댓값 구하기
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i  # 예산 - 부서별 신청 금액
        if budget >= 0:
            cnt += 1
        else:
            return cnt
    return cnt


# Solution_2 -> Solution_1과 비슷한 로직. 새로운 변수 생성 대신 index 사용
def solution(d, budget):
    d.sort()
    for cnt in range(len(d)):
        budget -= d[cnt]
        if budget < 0:
            return cnt
    return cnt + 1


# Solution_3 -> budget이 전체 d의 합보다 크거나 같을 때까지 d의 최댓값을 pop으로 제거. 조금 느림
# 만약, d의 길이가 매우 길고 budget이 작은 수일 경우, 계속해서 전체 리스트를 sum 해주므로 효율성 문제 발생 가능
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


# test case
print(solution([1, 3, 2, 5, 4], 9))  # 3
print(solution([2, 2, 3, 3], 10))    # 4