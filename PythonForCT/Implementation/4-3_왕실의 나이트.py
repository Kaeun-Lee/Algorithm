# Implementation

# Solution_1
location = input()
to_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
x, y = int(location[1]), to_num[location[0]]

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -2, 2]
dy = [-2, 2, 0, 0]

cnt = 0
for i in range(len(dx)):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:  # 체스판을 벗어나는 경우 무시
        continue
    elif abs(dx[i]) != 2:                     # 수평(L,R)으로 2칸 이동한 경우
        nx_p = nx + 1                         # 수직(아래)으로 1칸 이동
        nx_m = nx - 1                         # 수직(위)으로 1칸 이동
        if nx_p >= 1 and y >= 1 and nx_p <= 8 and y <= 8:
            cnt += 1
        if nx_m >= 1 and y >= 1 and nx_m <= 8 and y <= 8:
            cnt += 1
    else:                                     # 수직(U,D)으로 2칸 이동한 경우
        ny_p = ny + 1                         # 수평(오른쪽)으로 1칸 이동
        ny_m = ny - 1                         # 수평(왼쪽)으로 1칸 이동
        if x >= 1 and ny_p >= 1 and x <= 8 and ny_p <= 8:
            cnt += 1
        if x >= 1 and ny_m >= 1 and x <= 8 and ny_m <= 8:
            cnt += 1
    
print(cnt)


# Solution_2
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)



# test_case1
# 입력 : a1
# 출력 : 2

# test_case2
# 입력 : c2
# 출력 : 6