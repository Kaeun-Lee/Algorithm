#  Implementaion

n, m = map(int, input().split())
row, column, direction = map(int, input().split())
map = [[input()] for _ in range(n)]

start = (row, column)