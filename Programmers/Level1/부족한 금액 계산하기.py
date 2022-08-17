# 위클리 챌린지 | https://school.programmers.co.kr/learn/courses/30/lessons/82612

# Solution_1
def solution(price, money, count):
    a = sum(price * i for i in range(1, count + 1))
    return 0 if money >= a else a - money


# Solution_2 -> 등차수열의 합 공식 이용. 가장 빠름
# 등차수열의 합 : 1부터 n까지 숫자들의 합. n(n + 1) / 2
# n = count 변수. 아래 코드에서는 3 + 6 + 9 + 12 = 3 * (1 + 2 + 3 + 4)로 계산했음
def solution(price, money, count):
    return max(0, price * (count + 1) * count // 2 - money)


# Solution_3 
def solution(price, money, count):
    return abs(min(money - sum(price * i for i in range(1, count + 1)), 0))


# test case
print(solution(3, 20, 4))  # 10