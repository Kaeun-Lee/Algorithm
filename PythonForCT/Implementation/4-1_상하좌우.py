# Implementation

# Solution_1
size = int(input())
direction = list(input().split())
start = [1,1]

for i in direction:
    if i == 'R'and (start[1]+1 <= size):
        start[1] += 1
    elif i == 'L' and (start[1]-1 >= 1):
        start[1] -= 1
    elif i == 'D'and (start[0]+1 <= size):
        start[0] += 1
    elif i == 'U' and (start[0]-1 >= 1):
        start[0] -= 1
print(start[0], start[1])     


# Soluton_2
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]  # 이동 시 X축에서 계산되는 값
dy = [-1, 1, 0, 0]  # 이동 시 y축에서 계산되는 값
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)



# test_case1
# 입력 : 5
#        R R R U D D
# 출력 : 3 4