# 월간 코드 챌린지 시즌1 | https://school.programmers.co.kr/learn/courses/30/lessons/68935

# Solution_1
def solution(n):
    temp = ''
    result = 0
    while n // 3 > 0:      # 002
        temp += str(n % 3)
        n //= 3
    temp += str(n % 3)     # 0021
    temp = reversed(temp)  # 1200
    
    for i, n in enumerate(temp):
        result += (3 ** i) * int(n)
    return result


# Solution_2
# 1. n진수 만들기 : 입력 값이 0이 될 때까지, n으로 나눈 나머지를 모두 구해 역순으로 붙임(몫을 다시 n으로 나눔)
# 2. int(str, base) : n진법으로 이루어진 숫자 문자열 str과 n을 int 함수에 넣으면, 10진수로 값으로 변환됨
def solution(n):
    result = ''
    while n:  
        result += str(n % 3)
        n //= 3
    return int(result, 3)


# Solution_3 -> divmod() 이용. divmod(45, 3) = (15, 0)
def solution(n):
    result = ''
    while n > 0:  
        n, mod = divmod(n, 3)
        result += str(mod)
    return int(result, 3)


# Solution_4 -> divmod() 이용
def solution(n):
    answer = []
    while True:
        if n < 3:
            answer.append(n)
            break
        n, mod = divmod(n, 3)
        answer.append(mod)
    answer.reverse()
    sum_ = 0
    for i in range(len(answer)):
        sum_ += answer[i] * (3 ** i)
    return sum_

    
# test case
print(solution(45))   # 7
print(solution(125))  # 229