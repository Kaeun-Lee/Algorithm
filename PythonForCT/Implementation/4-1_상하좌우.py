# Implementation

# Solution_1
n = int(input())
map = input().split()

xy = (1, 1)

# 좌표
d = (1, 0)
u = (-1, 0)
r = (0, 1)
l = (0, -1)

for i in range(len(map)):
    if map[i] == 'D':
        temp_xy = (xy[0] + d[0], xy[1] + d[1])
    elif map[i] == 'U':
        temp_xy = (xy[0] + u[0], xy[1] + u[1])
    elif map[i] == 'R':
        temp_xy = (xy[0] + r[0], xy[1] + r[1])
    else:
        temp_xy = (xy[0] + l[0], xy[1] + l[1])
    if temp_xy[0] < 1 or temp_xy[0] > n or temp_xy[1] < 1 or temp_xy[0] > n:
        continue
    else:
        xy = temp_xy
print(xy[0], xy[1])


# Solution_2
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


# Soluton_3
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