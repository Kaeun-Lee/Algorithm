# Greedy

# Solution_1
a, b = map(int, input().split())

temperature = [10, 5, 1]

cnt = 0
start = abs(b - a)

for i in temperature:
    cnt += (start // i) # 몫, 가장 큰 수로 나눠지는 몫
    start %= i

print(cnt)  