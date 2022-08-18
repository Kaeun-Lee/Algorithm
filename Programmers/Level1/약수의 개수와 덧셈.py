# 월간 코드 챌린지 시즌2 | https://school.programmers.co.kr/learn/courses/30/lessons/77884

# Solution_1
def solution(left, right):
    result = 0
    for i in range(left, right + 1):  
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1): 
            if i % j == 0: 
                if j != i ** 0.5: 
                    cnt += 2
                else:
                    cnt += 1
        if cnt % 2 == 0:
            result += i
        else:
            result -= i
    return result


# Solution_2 -> 제곱수의 약수 개수는 홀수
def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            result -= i
        else:
            result += i
    return result


# Solution_3 -> Solution_2를 list comprehension으로 구현
def solution(left, right):
    return sum([-n if int(n ** 0.5) == n ** 0.5 else n for n in range(left, right + 1)]) 


# Solution_4
def solution(left, right):
    return sum([n if (n ** 0.5) % 1 else -n for n in range(left, right + 1)]) 

    
# test case
print(solution(13, 17))  # 43
print(solution(24, 27))  # 52
print(solution(1, 2))    # 1