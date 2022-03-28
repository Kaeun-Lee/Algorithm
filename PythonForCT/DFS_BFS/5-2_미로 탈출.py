# BFS

# Solution_1
from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for i in range(n)]

x, y = 0, 0
distance = 1

def bfs(maze, x, y, distance):
    queue = deque((x, y, distance))
   
    # 큐가 빌 때까지 반복
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        distance = queue.popleft()

        if x == n-1 and y == m-1 :
            print(distance)
            break
        else: 
            # 상, 하, 좌, 우
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 현재 maze라는 변수는 미로의 구조를 나타내기도 하고 출발점으로부터의 거리를 나타내기도 함
                # 따라서 출발점으로부터의 거리를 나타내는 변수를 따로 저장해두는 것이 안전한 코딩임
                # ex) distance = [[-1]*m for i in range(n)]에 거리 값을 저장
                # ex) distance = [[-1 for i in range(m)] for j in range(n)]
                # *주의* [[-1]*m]*n -> 이 경우 하나를 바꾸면 다른 것도 모두 바뀜!
                if nx >= 0 and nx < n and ny >= 0 and ny < m and maze[nx][ny] == 1: 
                    distance = maze[x][y] + 1
                    maze[nx][ny] = distance
                    queue.append(nx)
                    queue.append(ny)
                    queue.append(distance)
                    
bfs(maze, x, y, distance)    


# Solution_2
from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n -1][m -1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))



# test_case
# 입력
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 출력 : 10