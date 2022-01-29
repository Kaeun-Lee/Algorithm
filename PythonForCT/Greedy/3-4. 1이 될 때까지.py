# Greedy

# Solution_1
n, k = map(int, input().split())
cnt = 0

while True:
    if n % k != 0: # n이 k의 배수가 아닌 경우 1씩 빼면서 배수로 만듦
        n -= 1
        cnt += 1
    else:
        if n // k != 1: # 몫이 1이 아닌 경우
            n //= k
            cnt += 1
        else: # 몫이 1인 경우
            cnt += 1
            break 
        
print(cnt) # 3 | 2


# Solution_2
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k # 17 // 4 = 4, 4 * 4 = 16
    result += (n - target) # 17 - 16 = 1
    n = target # 16
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)



# 입력1
# 17 4

# 입력2
# 25 5