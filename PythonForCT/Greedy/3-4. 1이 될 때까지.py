# Greedy

# Solution_1
n, k = map(int, input().split())
cnt = 0

while True:
    if n == 1:
        break
    if n % k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt) 


# Solution_ 2 -> 일일이 1씩 빼는 방안
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 k로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1    
    
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)


# Solution_3 -> N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방안
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k   # 17 // 4 = 4, 4 * 4 = 16
    result += (n - target)  # 17 - 16 = 1
    n = target              # 16
    
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)



# test_case1
# 입력 : 17 4
# 출력 : 3

# test_case2
# 입력 : 25 5
# 출력 : 2

# test_case3
# 입력 : 25 3
# 출력 : 6

# test_case4
# 입력 : 127 4
# 출력 : 12