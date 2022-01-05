# 힙 | https://programmers.co.kr/learn/courses/30/lessons/42626

# Solution_1
import heapq
from collections import deque 
def solution(scoville, K):
    h = []
    sorted = []
    for v in scoville:
        heapq.heappush(h, v)
    
    for i in range(len(h)):
        sorted.append(heapq.heappop(h))
    a = heapq.heappop(sorted) # 최솟값
    if a < 7:
        b = heapq.heappop(sorted)
        sco = a + b*2
        sorted.insert(0, sco)
   
    cnt = 0
    sco = 0

    while sco >= K:
        a = heapq.heappop(sorted)
        b = heapq.heappop(sorted)
        sco = a + b*2
        cnt += 1
        sorted.insert(0,sco)
    return cnt