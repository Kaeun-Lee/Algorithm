# 연습문제 | https://school.programmers.co.kr/learn/courses/30/lessons/86491

# Solution_1
# [w, h]에서, 큰 사이즈 중 가장 큰 값 x 작은 사이즈 중 가장 큰 값
def solution(sizes):
    w = []
    h = []
    for i in sizes:
        w.append(max(i))
        h.append(min(i))
    return max(w) * max(h)


# Solution_2
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# Solution_3 -> heapq로 최대 힙 구현
def solution(sizes):
    import heapq
    mq_w, mq_h = [], []
    for size in sizes:
        w, h = size[0], size[1]
        if w < h:
            w, h = h, w
        heapq.heappush(mq_w, -w)  # [-80, -70, -60, -60] -> 최솟값이 가장 처음에 나옴
        heapq.heappush(mq_h, -h)  # [-50, -40, -30, -30]
    return mq_w[0] * mq_h[0]


# Solution_4 -> sorted 이용
def solution(sizes):
    sizes = [sorted(i) for i in sizes]
    return max(x[0] for x in sizes) * max(x[1] for x in sizes)


# Solution_5 -> sum 함수 활용. 속도 가장 느림
# sum(iterable, start=0)  -> start : 덧셈을 할 때, 제일 처음 시작하는 원소
# sum(sizes, []) : sizes라는 2차원 리스트를 1차원으로 풀어줌
# ex) sum([[1, 2], [3, 4]], []) : [] + [1, 2] + [3, 4] = [1, 2, 3, 4]
def solution(sizes):
    return max(sum(sizes, [])) * max(min(size) for size in sizes)


# test case
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))       # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133