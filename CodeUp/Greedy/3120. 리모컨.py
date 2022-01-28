# Greedy | https://codeup.kr/problem.php?id=3120

# Solution_1
a, b = map(int, input().split())

cnt = 0
start = abs(a-b)

while True:
    if start >= 8:                            # 8 이상인 수는 10부터 빼줌
        start -= 10
        cnt += 1
    elif start >= 3 and start < 8:            # 3이상 7이하인 수는 5부터 빼줌
        start -= 5
        cnt += 1
    elif abs(start) >= 1 and abs(start) < 3:  # 절댓값이 1이나 2인 경우엔 숫자 그대로 count함
        cnt += abs(start)
        break
    else:                                     # 0인 경우 
        break
    
print(cnt)  # 5 | 3



# 입력1
# 7 34 

# 입력2
# 22 3