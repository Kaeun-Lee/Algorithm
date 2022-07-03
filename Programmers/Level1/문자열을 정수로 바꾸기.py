# 연습문제 | https://programmers.co.kr/learn/courses/30/lessons/12925?language=python3

# Solution_1
def solution(s):
    sign = s[0]
    
    if sign == '-':
        return int(s[1:]) * -1
    return int(s)


# Solution_2 -> str을 정수형으로 변환하는 int 함수는 +, - 를 부호로 인식함
def solution(s):
    return int(s)


# Solution_3 -> 십진수 변환 접근법
# 만약 s가 0으로 시작할 수 있고, 주어진 문자열에 숫자와 문자열이 모두 포함될 수 있다는 등의 조건이 붙는다면, 이 풀이가 더 좋을 것임
def solution(s):
    result = 0

    for idx, number in enumerate(s[::-1]):  # -1234 -> 4321-
        if number == '-':
            result *= -1
        elif number == '+':
            result *= 1
        else:
            result += int(number) * (10**idx)  # 4 * (10 ** 0), 3 * (10 ** 1), ...

    return result


# test case
print(solution("1234"))   # 1234
print(solution("+1234"))  # 1234
print(solution("-1234"))  # -1234