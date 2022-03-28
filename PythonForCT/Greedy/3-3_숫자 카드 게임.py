# Greedy

# Solution_1 -> min() 함수 사용
row, column = map(int, input().split())

result = []
for i in range(row):
    min_num = min(list(map(int, input().split())))  # 각 행에서 가장 작은 수
    result.append(min_num)
    
print(max(result))                                  # 그 중 가장 큰 수


# Solution_2 -> Solution_1과 비슷한 풀이
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)


# Solution_3 -> 2중 반복문 구조를 이용
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)



# test_case1
# 입력 : 3 3
#        3 1 2
#        4 1 4
#        2 2 2
# 출력 : 2

# test_case2
# 입력 : 2 4
#        7 3 1 8
#        3 3 3 4
# 출력 : 3