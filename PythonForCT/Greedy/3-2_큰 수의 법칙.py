# Greedy

# 문제 : 주어진 배열의 수들을 M번 더하여 가장 큰 수를 만들기(특정 인덱스에 해당하는 수를 연속해서 K번까지만 더할 수 있음)
#        서로 다른 인덱스에 해당하는 수가 같은 경우, 서로 다른 것으로 간주


# Solution_1
# 아이디어 : 몫 * (가장 큰 수 K번 + 두 번째 큰 수 1번) + 나머지 * 가장 큰 수
n, m, k = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)  # 큰 수를 찾기 위한 내림차순 정렬

a = m // (k + 1)  # 몫
b = m % (k + 1)   # 나머지
result = (a * ((array[0] * k) + array[1])) + (b * array[0])  # 나머지가 있다면 (나머지 x 가장 큰 수)를 더해줌

print(result)


# Solution_2 -> 단순하게 푸는 답안 예시
n, m, k = map(int, input().split())     # N, M, K를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))  # N개의 수를 공백으로 구분하여 입력받기

data.sort()             # 입력받은 수들 정렬하기
first = data[n - 1]     # 가장 큰 수
second = data[n - 2]    # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:      # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1          # 더할 때마다 1씩 빼기
    if m == 0:          # m이 0이라면 반복문 탈출
        break
    result += second    # 두 번째로 큰 수를 한 번 더하기
    m -= 1              # 더할 때마다 1씩 빼기
    
print(result)           # 최종 답안 출력


# Solution_3 -> 간단한 수학적 아이디어(반복되는 수열)을 이용해 더 효율적으로 푸는 답안 예시
# 아이디어 : 가장 큰 수가 더해지는 횟수를 구하고, 이를 이용해 두 번째 큰 수가 더해지는 횟수를 구하여 각각 곱해줌
#           즉, 가장 큰 수가 더해지는 횟수 : int(M / (K + 1)) * K + M % (K + 1)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()          
first = data[n - 1]   
second = data[n - 2]  

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first       # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  


# test_case1
# input : 5 8 3
#         2 4 5 4 6
# output : 46

# test_case2
# input : 5 7 2
#         3 4 3 4 3
# output : 28