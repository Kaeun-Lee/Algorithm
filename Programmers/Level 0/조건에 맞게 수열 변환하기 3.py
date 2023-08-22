# 코딩테스트 입문


# My Solution -> else를 쓰지 않아도 됨
def solution(arr, k):
    if k % 2:
        return list(map(lambda x: x * k, arr))
    return list(map(lambda x: x + k, arr))


# Another Solution 1 -> map과 lambda를 사용한 solution보다 훨씬 빠름
def solution(arr, k):
    return [i * k if k % 2 else i + k for i in arr]


# Another Solution 2 -> 가장 빠름
def solution(arr, k):
    if k % 2:
        return [a * k for a in arr]
    return [a + k for a in arr]
    # return [a * k for a in arr] if k % 2 else [a + k for a in arr]
