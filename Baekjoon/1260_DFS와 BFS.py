# https://www.acmicpc.net/problem/1260 30 + 30

'''
문제 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력
      (정점 번호는 1 ~ N번. 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료)
'''

# Solution_1
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().rstrip().split())
edges = [list(map(int, input().split())) for _ in range(m)]  # 간선이 연결하는 두 정점의 번호
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for node in edges:
    if node[1] not in graph[node[0]]:
        graph[node[0]].append(node[1])
    if node[0] not in graph[node[1]]:
        graph[node[1]].append(node[0])

for node in graph:
    node.sort()

# dfs
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

   
# bfs
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    
dfs(graph, v, visited)
print(sep='')
visited = [False] * (n + 1)
bfs(graph, v, visited)