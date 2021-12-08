# 월간 코드 챌린지 시즌3 | https://programmers.co.kr/learn/courses/30/lessons/86051

# Solution_1
def solution(numbers):
    num = [0,1,2,3,4,5,6,7,8,9]
    answer = sum([i for i in num if i not in numbers])
    return answer


# Solution_2
def solution(numbers):  
    return 45 - sum(numbers)  # 배열의 합을 이용


# Solution_3
solution = lambda x : sum(range(10)) - sum(x)



test_case1 = solution([1,2,3,4,6,7,8,0])
test_case2 = solution([5,8,4,0,6,7,9])
print(test_case1)  # 14
print(test_case2)  # 6