# 피보나치 함수(Fibonacci Function)

# Solution_1 -> 일반적인 재귀 함수로 구현한 피보나치 함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))  # 3


# Solution_2 -> 다이나믹 프로그래밍 방법 중 '메모이제이션'을 사용한 피보나치 수열
d = [0] * 100  # 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화

# 피보나치 함수(Fibonacci Function)를 재귀 함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    # 현재 피보나치 수를 출력
    # print('f(' + str(x) + ')', end=' ')

    # 종료 조건(1 혹은 2일 때, 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면, 그대로 반환
    if d[x] != 0:
        return d[x]   
    # 아직 계산하지 않은 문제라면, 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))  # 218922995834555169026

# Solution_3 -> 반복문으로 구현한 피보나치 수열 
d = [0] * 100  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수(Fibonacci Function) 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])
