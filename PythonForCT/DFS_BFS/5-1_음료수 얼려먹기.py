# DFS

# Solution_1
n, m = map(int, input().split())
ice = [list(map(int, input())) for i in range(n)]
cnt = 0

def dfs(x, y):
    # 얼음틀을 벗어나는 경우 종료
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
     
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 상, 하, 좌, 우에 0이 있는 경우 1로 변경 후 재귀함수 호출
    if ice[x][y] == 0:
        ice[x][y] = 1
        for d in range(len(dx)):
            i = x + dx[d]
            j = y + dy[d]
            dfs(i, j)
        return True 

        
for i in range(n):
    for j in range(m):
        # 재귀함수 결과가 True면 count 증가
        if dfs(i, j) == True:
            cnt += 1
                
print(cnt)


# Solution_2
n, m = map(int, input().split())
graph = [list(map(int, input())) for i in range(n)]
cnt = 0

def dfs(x, y):
    graph[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 0:
            dfs(nx, ny)
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            cnt += 1
            
print(cnt)     


# Solution_3
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
            
print(result)



# test_case1
# 입력
# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 : 3

# test_case1
# 입력
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# 출력 : 8